# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os
from config import DS
import asyncio, re
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from .database import addCap, updateCap, chnl_ids
from pyrogram.types import Message
from datetime import timedelta    

# ===================== [ Set Caption Command ] ===================== #


@Client.on_message(filters.command(["setcap", "setcaption"]) & filters.channel)
async def setCaption(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Example: /setcap set your caption ( Use <code>{file_name}</code> or <code>{post_caption}</code> to show file name\nAlso Use <code>{file_size}</code> to show file size</b>\n\n<b>For More Information Give /help Command To Bot</b>)"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Successfully Saved Your Caption.\n\nYour New Caption: `{caption}`")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Successfully Saved Your Caption.\n\nYour New Caption: `{caption}`")


# ===================== [ Delete Caption Command ] ===================== #


@Client.on_message(filters.command(["delcap", "delcaption", "delete_caption"]) & filters.channel)
async def delCaption(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b>Successfully deleted your caption..From now i will use my default caption</b>")
    except Exception as e:
        ds = await msg.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await ds.delete()
        return


# ===================== [ Edit Caption In Channel ] ===================== #

"""
@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(file_name=file_name, file_size=get_size(file_size), post_caption = message.caption or message.text or "")
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = DS.DEF_CAP.format(file_name=file_name)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return
    """


@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption or message.text or ""
    
    # Function to format duration to HH:MM:SS
    def format_duration(duration: int):
        return str(timedelta(seconds=duration))

    if message.media:
        media_type = message.media.media_type  # Extract media type
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)

                # Clean the file name
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )

                # Extract media duration if available
                duration = 0  # Default to 0
                if media_type == "video" and obj.duration:
                    duration = obj.duration  # Video duration in seconds
                elif media_type == "audio" and obj.duration:
                    duration = obj.duration  # Audio duration in seconds

                # Get caption details from the database
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(
                            file_name=file_name,
                            file_size=get_size(file_size),
                            file_caption=default_caption,
                            language=language,
                            year=year,
                            file_type=media_type,
                            duration=format_duration(duration)  # Include duration in caption
                        )
                        await message.edit(replaced_caption) 
                    else:
                        replaced_caption = DEF_CAP.format(file_name=default_caption)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return

# ===================== [ Size Conversion Function ] ===================== #


def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

# ===================== [ Quality Extract Function ] ===================== #

def extract_quality(default_caption):
    quality_pattern = r'\b(2160p|4k|1440p|1080p|720p|575p|560p|480p|360p|240p)\b(?:\s+(HEVC))?'
    qualities = set(re.findall(quality_pattern, default_caption, re.IGNORECASE))
    if not qualities:
        return "Unknown Quality"
    return ", ".join(sorted(qualities, key=str.lower))

# ===================== [ Language Extraction Function ] ===================== #

def extract_language(default_caption):
    language_pattern = r'\b(Hindi|hindi|hin|Marathi|mar|marathi|English|Eng|eng|english|Gujarati|gujarati|Guj|guj|Tamil|Tam|tamil|tam|Telugu|telugu|tel|Tel|Malayalam|malayalam|Mal|mal|Kannada|kan|Kan|kannada|Hin)\b'#Contribute More Language If You Have
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    if not languages:
        return "Hindi-English"
    return ", ".join(sorted(languages, key=str.lower))

# ===================== [ Year Extract Function ] ===================== #

def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

# ===================== [🔺 End Of Caption.py 🔺] ===================== #
