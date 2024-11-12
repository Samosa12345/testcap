# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os
from config import DS
from magic import Magic
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
    


@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption or message.text or ""
    
    # Function to format duration to HH:MM:SS
    def format_duration(duration: int):
        return str(timedelta(seconds=duration))

    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)
                quality = extract_quality(default_caption)
        
                # Clean the file name
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )

                
                mime_type = "Unknown"
                if hasattr(message.media, "mime_type"):
                    mime_type = message.media.mime_type

                duration = "Unknown"
                if media_type == "Video" and hasattr(message.media, "duration"):  # Only for videos
                    duration = message.media.duration
                elif media_type == "Audio" and hasattr(message.media, "duration"):  # Only for audio
                    duration = message.media.duration

                media_type = "Unknown"  # This is what you're trying to determine
                if message.photo:
                    media_type = "Photo"
                elif message.video:
                    media_type = "Video"
                elif message.document:
                    media_type = "Document"
                elif message.audio:
                    media_type = "Audio"
                elif message.voice:
                    media_type = "Voice Note" 
                
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
                            quality=quality,
                            file_type=media_type,
                            duration=format_duration(duration),  # Include duration in caption
                            mime_type=mime_type
                        )
                        await message.edit(replaced_caption) 
                    else:
                        replaced_caption = DEF_CAP.format(file_name=default_caption)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return"""

@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption or message.text or ""

    # Function to format duration to HH:MM:SS
    #def format_duration(duration: int):
        #return str(timedelta(seconds=duration))

    ds = message.media
    def get_mime_type(ds):
    mime = Magic(mime=True)
    mimetype = mime.from_file(ds)
    mimetype = mimetype or "text/plain"
    return mimetype
    
    """if message.media:
        # Check the file type for duration and mime_type
        file_type = None
        obj = None
        media_type = "Unknown"
        #duration = "Unknown"
        mime_type = "Unknown"

        if message.video:
            file_type = "video"
            obj = message.video
            media_type = "Video"
            if hasattr(obj, "duration"):
                duration = obj.duration
            if hasattr(message.media, "mime_type"):
                mime_type = message.media.mime_type
        elif message.audio:
            file_type = "audio"
            obj = message.audio
            media_type = "Audio"
            if hasattr(obj, "duration"):
                duration = obj.duration
            if hasattr(message.media, "mime_type"):
                mime_type = message.media.mime_type
        elif message.document:
            file_type = "document"
            obj = message.document
            media_type = "Document"
            if hasattr(message.media, "mime_type"):
                mime_type = message.media.mime_type
        elif message.voice:
            file_type = "voice"
            obj = message.voice
            media_type = "Voice Note"
            if hasattr(message.media, "mime_type"):
                mime_type = message.media.mime_type"""

        if file_type in ("audio", "video", "voice"):
                    if obj.duration:
                        hours = int(obj.duration // 3600)
                        minutes = int((obj.duration % 3600) // 60)
                        seconds = int(obj.duration % 60)
                        if hours > 0:
                            duration = f"{hours} Hr {minutes} Min {seconds} Sec"
                        else:
                            duration = f"{minutes} Min {seconds} Sec"
                    else:
                        duration = ""
        # If there's a valid object with a file name, proceed to clean and process
        if obj and hasattr(obj, "file_name"):
            file_name = obj.file_name
            file_size = obj.file_size
            language = extract_language(default_caption)
            year = extract_year(default_caption)
            quality = extract_quality(default_caption)

            # Clean the file name
            file_name = (
                re.sub(r"@\w+\s*", "", file_name)
                .replace("_", " ")
                .replace(".", " ")
            )

            # Format the duration to HH:MM:SS if available
            """if isinstance(duration, int):
                duration = format_duration(duration)
            else:
                duration = "Unknown""""

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
                        mimetype=mimetype,
                        file_type=media_type,
                        duration=duration,  # Include formatted duration in caption
                      #  mime_type=mime_type,
                        quality=quality
                    )
                    await message.edit(replaced_caption)
                else:
                    replaced_caption = DEF_CAP.format(file_name=default_caption)
                    await message.edit(replaced_caption)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                # Retry the edit after waiting
                

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

# Extract video quality from caption
def extract_quality(default_caption):
    # Updated regex for quality (with optional HEVC tag)
    quality_pattern = r'\b(2160p|4k|1440p|1080p|720p|576p|560p|480p|360p|240p)\b(?:\s*(HEVC))?'
    
    # Find all matches, capturing quality and HEVC
    qualities = set(re.findall(quality_pattern, default_caption, re.IGNORECASE))
    
    if not qualities:
        return "Unknown Quality"
    
    # Only return the quality, optionally including 'HEVC' if it was matched
    result = []
    for quality, hevc in qualities:
        result.append(quality)
        if hevc:
            result.append(f"HEVC")  # Ensure HEVC is in uppercase
    return ", ".join(sorted(result, key=str.lower))

# ===================== [ Language Extraction Function ] ===================== #

# Extract language(s) from caption
def extract_language(default_caption):
    # Optimized regex for language detection
    language_pattern = r'\b(Hindi|hindi|hin|Marathi|mar|marathi|English|Eng|eng|english|Gujarati|gujarati|Guj|guj|Tamil|Tam|tamil|tam|Telugu|telugu|tel|Tel|Malayalam|malayalam|Mal|mal|Kannada|kan|Kan|kannada|Hin)\b'
    
    # Find all matches (case insensitive)
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    
    if not languages:
        return "Hindi-English"  # Default fallback
    
    # Sort languages alphabetically and return as comma-separated string
    return ", ".join(sorted(languages, key=str.lower))


# ===================== [ Year Extract Function ] ===================== #

def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

# ===================== [🔺 End Of Caption.py 🔺] ===================== #
