import os, tempfile, asyncio, aiofiles
from flask import Flask
from threading import Thread
from typing import Optional
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name="DSBot")

SECTION_ICONS = {
    "General": "📄",
    "Video": "🎞️",
    "Audio": "🎵",
    "Text": "🔤",
    "Image": "🖼️",
    "Menu": "📋"
}

def format_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def get_media_from_message(message: Message):
    return message.document or message.video or message.audio

async def stream_media(message: Message, temp_path: str, limit: int = 1) -> Optional[str]:
    try:
        media = get_media_from_message(message)
        if not media:
            return None

        async with aiofiles.open(temp_path, 'wb') as file:
            downloaded_chunks = 0
            async for chunk in app.stream_media(media, limit=limit):
                await file.write(chunk)
                downloaded_chunks += 1
                if downloaded_chunks >= limit:
                    break
        return temp_path
    except Exception as e:
        logger.error(f"Error streaming media: {e}")
        return None

async def get_mediainfo(file_path: str) -> str:
    try:
        process = await asyncio.create_subprocess_exec(
            'mediainfo', file_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if stderr:
            logger.warning(f"MediaInfo stderr: {stderr.decode()}")
        return stdout.decode()
    except Exception as e:
        logger.error(f"Error getting mediainfo: {e}")
        return ""

def parse_mediainfo(mediainfo_output, file_name, file_size):
    def clean(value: str) -> str:
        return value.replace('<', '&lt;').replace('>', '&gt;')

    html = ["<h3>📁 Media Information</h3>", "<hr>"]
    current_section = ""
    content = []

    for line in mediainfo_output.splitlines():
        line = line.strip()
        if not line:
            continue
        if any(line.startswith(section) for section in SECTION_ICONS):
            if current_section and content:
                content_str = "\n".join(content)
                icon = SECTION_ICONS.get(current_section, "📄")
                html.append(f"<h4>{icon} {current_section}</h4><pre>{content_str}</pre><br>")
            current_section = line
            content = []
        else:
            if current_section == "General" and line.lower().startswith("file size"):
                line = f"File size                                : {format_size(file_size)}"
            content.append(clean(line))

    if current_section and content:
        content_str = "\n".join(content)
        icon = SECTION_ICONS.get(current_section, "📄")
        html.append(f"<h4>{icon} {current_section}</h4><pre>{content_str}</pre><br>")

    return "\n".join(html)

async def create_telegraph_page(title: str, content: str) -> Optional[str]:
    try:
        clean_title = title[:128]
        response = telegraph.create_page(
            title=clean_title,
            html_content=content,
            author_name="DS MEDIA INFO BOT",
            author_url="https://t.me/DS_Mediainfo_Bot"
        )
        url = f"https://graph.org/{response['path']}"
        async with ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    logger.error(f"Created page not accessible: {resp.status}")
                    return None
        return url
    except Exception as e:
        logger.error(f"Error creating Telegraph page: {e}", exc_info=True)
        return None

async def process_media(message: Message):
    media = message.document or message.video or message.audio
    if not media:
        return await status.edit("❌ No media found!")

    file_name = getattr(media, 'file_name', 'Unknown')
    file_size = getattr(media, 'file_size', 0)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        temp_path = tmp.name

    try:
        path = await stream_media(message, temp_path)
        if not path:
            return await message.reply_text("❌ Download failed.")
        info = await get_mediainfo(path)
        if not info:
            return await message.reply_text("❌ Failed to get media info.")
        html = parse_mediainfo(info, file_name, file_size)
        url = await create_telegraph_page(file_name, html)
        if not url:
            return await message.reply_text("❌ Telegraph page creation failed.")
        keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 View Media Info", url=url)]
    ])
        await message.reply_text(f"**Mᴇᴅɪᴀ Iɴғᴏ Gᴇɴᴇʀᴀᴛᴇᴅ!**\n\n📁 **ғɪʟᴇ:** `{file_name}`\n\n💾 **Sɪᴢᴇ:** `{format_size(file_size)}`\n\n🤖 **[DS Mediainfo Bot](https://t.me/DS_Mediainfo_Bot)**",
            reply_markup=keyboard,
            disable_web_page_preview=True,
    )
    finally:
        os.unlink(temp_path)
      
@app.on_message(filters.channel & (filters.video | filters.document | filters.audio))
async def on_channel_media(client: Client, message: Message):
    media = get_media_from_message(message)
    if not media:
        return

    file_name = getattr(media, 'file_name', 'Unknown')
    file_size = getattr(media, 'file_size', 0)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name

    try:
        downloaded_path = await stream_media(message, temp_path)
        if not downloaded_path:
            return

        mediainfo_output = await get_mediainfo(downloaded_path)
        html_content = parse_mediainfo(mediainfo_output, file_name, file_size)

        telegraph_url = await create_telegraph_page(
            title=f"{file_name} - Media Info",
            content=html_content
        )

        if telegraph_url:
            button = InlineKeyboardMarkup([
                [InlineKeyboardButton("📋 View Media Info", url=telegraph_url)]
            ])
            await client.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=message.id,
                reply_markup=button
            )
    finally:
        try:
            os.unlink(temp_path)
        except Exception as e:
            logger.error(f"Error deleting temp file: {e}")
          
@app.on_message(filters.command(["mediainfo", "mi"]))
async def mediainfo_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a media file!")
    await process_media(message.reply_to_message)
