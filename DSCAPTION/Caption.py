# (c) @Bisal & (c) @Sanchit0102

# ===================== [ Importing Requirements ] ===================== #
import os
import re
import datetime
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from .database import addCap, updateCap, chnl_ids
from config import DS

# ===================== [ Set Caption Command ] ===================== #

@Client.on_message(filters.command(["setcap", "setcaption"]) & filters.channel)
async def set_caption(bot, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Example:</b> /setcap Your caption here. Use <code>{filename}</code>, <code>{filesize}</code>, etc.\n<b>Use /variables to see all placeholders.</b>"
        )

    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1]
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})

    if chk_data:
        await updateCap(chnl_id, caption)
    else:
        await addCap(chnl_id, caption)

    await message.reply(f"Your new caption is:\n<code>{caption}</code>")


# ===================== [ Delete Caption Command ] ===================== #

@Client.on_message(filters.command(["delcap", "delcaption", "delete_caption"]) & filters.channel)
async def delete_caption(_, message: Message):
    chnl_id = message.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        await message.reply("<b>Successfully deleted your custom caption. Default will now be used.</b>")
    except Exception as e:
        reply = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await reply.delete()


# ===================== [ Caption Replacer Code Functions ] ===================== #

def get_wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    return "Good Night"

def get_size(size_bytes):
    size = float(size_bytes)
    for unit in ["Bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def extract_from_filename(name):
    patterns = {
        "year": r"\\b(19\\d{2}|20\\d{2})\\b",
        "quality": r"(144p|240p|360p|480p|720p|1080p|2160p|4k)",
        "season": r"s(\\d{1,2})",
        "episode": r"e(\\d{1,2})",
        "language": r"(hindi|english|tamil|telugu|malayalam|kannada|punjabi|marathi|gujarati|dual)",
        "ext": r"\\.([a-z0-9]+)$"
    }
    name_lower = name.lower()
    return {key: (re.search(pat, name_lower).group(1) if re.search(pat, name_lower) else "N/A") for key, pat in patterns.items()}

def format_caption(template, file_name, file_size, caption="", duration=None, height=None, width=None, mime_type=None, media_type=None, title=None, artist=None):
    info = extract_from_filename(file_name)
    resolution = f"{width}x{height}" if width and height else "N/A"
    
    placeholders = {
        "{filename}": file_name,
        "{filesize}": get_size(file_size),
        "{caption}": caption or "",
        "{language}": info["language"],
        "{year}": info["year"],
        "{quality}": info["quality"],
        "{season}": info["season"],
        "{episode}": info["episode"],
        "{duration}": duration or "N/A",
        "{height}": str(height or "N/A"),
        "{width}": str(width or "N/A"),
        "{resolution}": resolution,
        "{ext}": info["ext"],
        "{mime_type}": mime_type or "N/A",
        "{media_type}": media_type or "N/A",
        "{title}": title or "N/A",
        "{artist}": artist or "N/A",
        "{wish}": get_wish()
    }

    for key, val in placeholders.items():
        template = template.replace(key, str(val))
    return template

# ===================== [ Main Channel Message Handler ] ===================== #

@Client.on_message(filters.channel)
async def handle_channel_message(bot, message: Message):
    chnl_id = message.chat.id
    file = message.document or message.video or message.audio

    if not file:
        return

    cap_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    template = cap_data["caption"] if cap_data else DS.DEF_CAP

    edited_caption = format_caption(
        template,
        file_name=file.file_name,
        file_size=file.file_size,
        caption=message.caption,
        duration=getattr(file, "duration", None),
        height=getattr(file, "height", None),
        width=getattr(file, "width", None),
        mime_type=getattr(file, "mime_type", None),
        media_type="Document" if message.document else "Video" if message.video else "Audio",
        title=getattr(file, "title", None),
        artist=getattr(file, "performer", None)
    )

    await message.edit(edited_caption)

# ===================== [ Show Placeholder Variables ] ===================== #

@Client.on_message(filters.command("variables"))
async def show_placeholders(_, message: Message):
    text = """<b>
⋗ {filename} = File name.
⋗ {filesize} = Original file size.
⋗ {caption} = File caption.
⋗ {language} = Languages extracted from the file name.
⋗ {year} = Year extracted from the file name.
⋗ {quality} = Quality extracted from the file name.
⋗ {season} = Season extracted from the file name.
⋗ {episode} = Episode extracted from the file name.
⋗ {duration} = Duration of the file (for videos/audio).
⋗ {height} = Height of the video.
⋗ {width} = Width of the video.
⋗ {resolution} = Resolution (e.g., 1920x1080).
⋗ {ext} = File extension (e.g., mp4, mkv).
⋗ {media_type} = Type of media (e.g., video, document)
⋗ {mime_type} = Mime type of the file (video/mp4, audio/mpeg, etc.).
⋗ {title} = Title of the audio.
⋗ {artist} = Artist of the audio.
⋗ {wish} = Good Morning / Afternoon / Evening / Night
</b>"""
    await message.reply(text)
    
