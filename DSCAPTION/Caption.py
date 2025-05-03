# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os, datetime, asyncio, re
from config import DS
from .database import *    
from pyrogram.types import *
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from .database import addCap, updateCap, chnl_ids

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
        return await message.reply(f"Your New Caption is: `{caption}`")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Your Caption is: `{caption}`")


# ===================== [ Delete Caption Command ] ===================== #

@Client.on_message(filters.command(["delcap", "delcaption", "delete_caption"]) & filters.channel)
async def delCaption(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b>Successfully deleted your caption. Using default caption now</b>")
    except Exception as e:
        ds = await msg.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await ds.delete()
        return

# ===================== [ Edit Caption In Channel ] ===================== #

# Get wish based on time
def get_wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])
    
# Extract metadata from filename
def extract_from_filename(name):
    patterns = {
        "year": r'\b(19\d{2}|20\d{2})\b',
        "quality": r'(144p|240p|360p|480p|720p|1080p|2160p|4k)',
        "season": r's(\d{1,2})',
        "episode": r'e(\d{1,2})',
        "language": r'(hindi|marathi|punjabi|gujarati|english|telugu|tamil|malayalam|kannada|dual)',
        "ext": r'\.([a-z0-9]+)$'
    }
    name_lower = name.lower()
    data = {key: re.search(pattern, name_lower).group(1) if re.search(pattern, name_lower) else "N/A" for key, pattern in patterns.items()}
    return data

# Format caption with placeholders
def format_caption(template, file_name, file_size, caption="", duration=None, height=None, width=None, mime_type=None, title=None, artist=None):
    file_info = extract_from_filename(file_name)
    resolution = f"{width}x{height}" if width and height else "N/A"

    placeholders = {
        "{filename}": file_name,
        "{filesize}": file_size,
        "{caption}": caption or "",
        "{language}": file_info["language"],
        "{year}": file_info["year"],
        "{quality}": file_info["quality"],
        "{season}": file_info["season"],
        "{episode}": file_info["episode"],
        "{duration}": duration or "N/A",
        "{height}": str(height) if height else "N/A",
        "{width}": str(width) if width else "N/A",
        "{resolution}": resolution,
        "{ext}": file_info["ext"],
        "{mime_type}": mime_type or "N/A",
        "{title}": title or "N/A",
        "{artist}": artist or "N/A",
        "{wish}": get_wish()
    }

    for key, value in placeholders.items():
        template = template.replace(key, str(value))

    return template

# Function to process files in batch and rename captions
async def process_files_in_batch(message, cap_dets, files_data):
    tasks = []
    for file_data in files_data:
        file_name = file_data["file_name"]
        file_size = file_data["file_size"]
        default_caption = message.caption
        duration = file_data.get('duration', None)
        height = file_data.get('height', None)
        width = file_data.get('width', None)
        mime_type = file_data.get('mime_type', None)
        title = file_data.get('title', None)
        artist = file_data.get('artist', None)

        # Get caption template from DB or default
        caption = cap_dets["caption"] if cap_dets else DS.DEF_CAP
        replaced_caption = format_caption(caption, file_name, file_size=get_size(file_size), default_caption, duration, height, width, mime_type, title, artist)
        
        # Create a task to edit the caption asynchronously
        tasks.append(message.edit(replaced_caption))

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

# Function to handle caption update for multiple files
@Client.on_message(filters.channel)
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption

    # Extract file data from message
    files_data = []
    for file_type in ("video", "audio", "document", "voice"):
        obj = getattr(message, file_type, None)
        if obj and hasattr(obj, "file_name"):
            files_data.append({
                "file_name": obj.file_name,
                "file_size": obj.file_size,
                "duration": getattr(obj, 'duration', None),
                "height": getattr(obj, 'height', None),
                "width": getattr(obj, 'width', None),
                "mime_type": getattr(obj, 'mime_type', None),
                "title": getattr(obj, 'title', None),
                "artist": getattr(obj, 'performer', None),
            })

    # Fetch caption template from database
    cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})

    # Process all files in batch
    await process_files_in_batch(message, cap_dets, files_data)

# Command to show available placeholders for caption usage
@Client.on_message(filters.command("variables"))
async def show_placeholders(bot, message):
    placeholders_info = """<b>
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
⋗ {mime_type} = Mime type of the file (video/mp4, audio/mpeg, etc.).
⋗ {title} = Title of the audio.
⋗ {artist} = Artist of the audio.
⋗ {wish} = A greeting based on time of day (e.g., Good Morning, Good Evening).
    </b>"""
    await message.reply(placeholders_info)
