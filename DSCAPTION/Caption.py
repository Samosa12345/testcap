# (c) @Bisal & (c) @Sanchit0102

import os
import re
import datetime
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from .database import addCap, updateCap, chnl_ids
from config import DS

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

def clean_filename(name):
    name = name.strip()
    name_without_ext, ext = os.path.splitext(name)
    name_cleaned = re.sub(r'[\._]+', ' ', name_without_ext)  # Replace dots/underscores with space
    name_cleaned = re.sub(r'\s{2,}', ' ', name_cleaned).strip()  # Remove extra spaces
    return f"{name_cleaned}{ext}"
    
"""def clean_filename(name):
    name = re.sub(r"[._]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    name = re.sub(r"\s+(\.\w{2,4})$", r"\1", name)  # keep extension
    return name
"""
def format_duration(seconds):
    if not seconds:
        return "N/A"
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, sec = divmod(remainder, 60)
    return f"{hours:02d} | {minutes:02d} | {sec:02d}"

"""def extract_from_filename(name):
    name_lower = name.lower()
    name_lower = name_lower.replace(".", " ").replace("_", " ")

    languages = [
        "hindi", "english", "tamil", "telugu", "malayalam", "kannada", "bengali",
        "marathi", "gujarati", "punjabi", "urdu", "french", "spanish", "korean",
        "japanese", "german", "chinese", "dual", "multi"
    ]
    found_languages = [lang.capitalize() for lang in languages if lang in name_lower]

    return {
        "year": re.search(r"\\b(19\\d{2}|20\\d{2})\\b", name_lower).group(1) if re.search(r"\\b(19\\d{2}|20\\d{2})\\b", name_lower) else "N/A",
        "quality": re.search(r"(144p|240p|360p|480p|720p|1080p|2160p|4k)", name_lower).group(1) if re.search(r"(144p|240p|360p|480p|720p|1080p|2160p|4k)", name_lower) else "N/A",
        "season": re.search(r"s(\\d{1,2})", name_lower).group(1) if re.search(r"s(\\d{1,2})", name_lower) else "N/A",
        "episode": re.search(r"e(\\d{1,4})", name_lower).group(1) if re.search(r"e(\\d{1,4})", name_lower) else "N/A",
        "language": ", ".join(found_languages) if found_languages else "N/A",
        "ext": re.search(r"\.([a-z0-9]{2,4})$", name.lower()).group(1) if re.search(r"\.([a-z0-9]{2,4})$", name.lower()) else "N/A"
    }
"""
def extract_from_filename(name):
    name_cleaned = re.sub(r"[._]+", " ", name).strip().lower()

    patterns = {
        "year": r"\b(19[0-9]{2}|20[0-4][0-9]|2050)\b",
        "quality": r"\b(144p|240p|360p|480p|720p|1080p|2160p|4k|hdr)\b",
        "season": r"(?:s|season[\s._-]?)(\d{1,2})",
        "episode": r"(?:e|ep|episode[\s._-]?)(\d{1,4})",
        "language": r"\b(hindi|english|tamil|telugu|malayalam|kannada|punjabi|marathi|gujarati|bengali|urdu|french|german|spanish|korean|japanese|dual|multi|dubbed|subbed|mandarin|russian|chinese|thai)\b",
        "ext": r"\.([a-z0-9]{2,5})$"
    }

    results = {}
    for key, pat in patterns.items():
        match = re.search(pat, name_cleaned, re.IGNORECASE)
        if match:
            results[key] = match.group(1).title() if key == "language" else match.group(1)
        else:
            results[key] = "N/A"

    return results

def format_caption(template, file_name, file_size, caption="", duration=None, height=None, width=None, mime_type=None, media_type=None, title=None, artist=None):
    info = extract_from_filename(file_name)
    resolution = f"{width}x{height}" if width and height else "N/A"
    clean_name = clean_filename(file_name)

    placeholders = {
        "{filename}": clean_name,
        "{filesize}": get_size(file_size),
        "{caption}": caption or "",
        "{language}": info["language"],
        "{year}": info["year"],
        "{quality}": info["quality"],
        "{season}": info["season"],
        "{episode}": info["episode"],
        "{duration}": format_duration(duration),
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
⋗ {duration} = Duration in Hour | Min | Sec.
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
    
