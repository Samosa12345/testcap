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

@Client.on_message(filters.command(["preview", "showcap"]) & filters.channel)
async def preview_caption(_, message: Message):
    chnl_id = message.chat.id
    cap_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if cap_data and "caption" in cap_data:
        await message.reply(f"<b>Your saved caption template:</b>\n<code>{cap_data['caption']}</code>")
    else:
        await message.reply("<b>No custom caption set. Default will be used.</b>")

@Client.on_message(filters.command("variables") & filters.channel)
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
    name_without_ext = os.path.splitext(name)[0]
    clean = re.sub(r'[._]+', ' ', name_without_ext).strip()
    return f"{clean}{os.path.splitext(name)[1]}"
    
def format_duration(seconds):
    if not seconds:
        return "N/A"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{int(hours):02d}h {int(minutes):02d}m {int(sec):02d}s"

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

def extract_episode_range(name):
    episodes = re.findall(r'e(\d{2,4})', name.lower())
    if not episodes:
        return "N/A"
    episodes = sorted(set(int(ep) for ep in episodes))
    if len(episodes) == 1:
        return f"{episodes[0]:02d}"
    return f"{episodes[0]:02d}-{episodes[-1]:02d}"

def extract_languages(name):
    name_lower = name.lower()

    language_map = {
        'hin': 'Hindi', 'hindi': 'Hindi',
        'tam': 'Tamil', 'tamil': 'Tamil',
        'tel': 'Telugu', 'telugu': 'Telugu',
        'mal': 'Malayalam', 'malayalam': 'Malayalam',
        'kan': 'Kannada', 'kannada': 'Kannada',
        'pun': 'Punjabi', 'punjabi': 'Punjabi',
        'mar': 'Marathi', 'marathi': 'Marathi',
        'guj': 'Gujarati', 'gujarati': 'Gujarati',
        'ben': 'Bengali', 'bengali': 'Bengali',
        'urd': 'Urdu', 'urdu': 'Urdu',
        'ori': 'Odia', 'odia': 'Odia',
        'ass': 'Assamese', 'assamese': 'Assamese',

        'eng': 'English', 'english': 'English',
        'fre': 'French', 'french': 'French',
        'ger': 'German', 'german': 'German',
        'spa': 'Spanish', 'spanish': 'Spanish',
        'ita': 'Italian', 'italian': 'Italian',
        'jap': 'Japanese', 'japanese': 'Japanese',
        'chi': 'Chinese', 'chinese': 'Chinese',
        'kor': 'Korean', 'korean': 'Korean',
        'rus': 'Russian', 'russian': 'Russian',
        'ara': 'Arabic', 'arabic': 'Arabic',
        'por': 'Portuguese', 'portuguese': 'Portuguese',
        'tur': 'Turkish', 'turkish': 'Turkish'
    }

    found = set()
    for key, lang in language_map.items():
        if re.search(rf'(?<!\w){key}(?!\w)', name_lower):
            found.add(lang)

    lang_list = sorted(found)

    if 'dual' in name_lower and lang_list:
        return f"Dual - {', '.join(lang_list)}"
    elif 'multi' in name_lower and lang_list:
        return f"Multi - {', '.join(lang_list)}"
    elif lang_list:
        return ', '.join(lang_list)
    else:
        return "N/A"
        
LANGUAGE_MAP = {  
    'ori': 'Odia', 'odia': 'Odia',
    'ass': 'Assamese', 'assamese': 'Assamese',
    'tur': 'Turkish', 'turkish': 'Turkish',
    "eng": "English", "english": "English",
    "hin": "Hindi", "hindi": "Hindi",
    "tam": "Tamil", "tamil": "Tamil",
    "tel": "Telugu", "telugu": "Telugu",
    "mal": "Malayalam", "malayalam": "Malayalam",
    "kan": "Kannada", "kannada": "Kannada",
    "mar": "Marathi", "marathi": "Marathi",
    "guj": "Gujarati", "gujarati": "Gujarati",
    "ben": "Bengali", "bengali": "Bengali",
    "pun": "Punjabi", "punjabi": "Punjabi",
    "urdu": "Urdu", "urdu": "Urdu",
    "jap": "Japanese", "japanese": "Japanese",
    "chi": "Chinese", "chinese": "Chinese",
    "kor": "Korean", "korean": "Korean",
    "fre": "French", "french": "French",
    "ger": "German", "german": "German",
    "ita": "Italian", "italian": "Italian",
    "spa": "Spanish", "spanish": "Spanish",
    "arab": "Arabic", "arabic": "Arabic",
    "port": "Portuguese", "portuguese": "Portuguese",
    "rus": "Russian", "russian": "Russian",
    "nep": "Nepali", "nepali": "Nepali",
    "san": "Sanskrit", "sanskrit": "Sanskrit",
    "lat": "Latin", "latin": "Latin"
}
LANG_MAP = {  
    'ori': 'Odia', 'odia': 'Odia',
    'ass': 'Assamese', 'assamese': 'Assamese',
    'tur': 'Turkish', 'turkish': 'Turkish',
    "eng": "English", "english": "English",
    "hin": "Hindi", "hindi": "Hindi",
    "tam": "Tamil", "tamil": "Tamil",
    "tel": "Telugu", "telugu": "Telugu",
    "mal": "Malayalam", "malayalam": "Malayalam",
    "kan": "Kannada", "kannada": "Kannada",
    "mar": "Marathi", "marathi": "Marathi",
    "guj": "Gujarati", "gujarati": "Gujarati",
    "ben": "Bengali", "bengali": "Bengali",
    "pun": "Punjabi", "punjabi": "Punjabi",
    "urdu": "Urdu", "urdu": "Urdu",
    "jap": "Japanese", "japanese": "Japanese",
    "chi": "Chinese", "chinese": "Chinese",
    "kor": "Korean", "korean": "Korean",
    "fre": "French", "french": "French",
    "ger": "German", "german": "German",
    "ita": "Italian", "italian": "Italian",
    "spa": "Spanish", "spanish": "Spanish",
    "arab": "Arabic", "arabic": "Arabic",
    "port": "Portuguese", "portuguese": "Portuguese",
    "rus": "Russian", "russian": "Russian",
    "nep": "Nepali", "nepali": "Nepali",
    "san": "Sanskrit", "sanskrit": "Sanskrit",
    "lat": "Latin", "latin": "Latin"
}

def extract_metadata(name: str, caption: str = "") -> dict:
    text = f"{name} {caption}".lower()

    # Season detection
    season_match = re.search(r'(?:s|season)[\s\._-]*(\d+)', text, re.IGNORECASE)
    season = season_match.group(1) if season_match else None

    # Updated and more precise episode parsing
    episode_patterns = [
        r'[Ss]eason[ _.-]*([0-9]{1,2})[^\n\r]*?[Ee]pisode[ _.-]*([0-9]{1,2})(?:\s*(?:to|-|–)\s*([0-9]{1,2}))?',
        r'[Ss]([0-9]{1,2})[^\n\r]*?[Ee]([0-9]{1,2})(?:\s*(?:to|-|–)\s*([0-9]{1,2}))?',
        r'[Ss]eason[ _.-]*([0-9]{1,2})[^\n\r]*?[Ee]p?[ _.-]*([0-9]{1,2})(?:\s*(?:to|-|–)\s*([0-9]{1,2}))?',
    ]

    episode = "N/A"
    for pattern in episode_patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if not match:
            match = re.search(pattern, caption or "", re.IGNORECASE)
        if match:
            season_num = match.group(1)
            episode_start = match.group(2)
            episode_end = match.group(3) if len(match.groups()) > 2 and match.group(3) else None

        # Ensure we're not capturing a 4-digit year as episode
            if episode_start and len(episode_start) == 4:
                continue
 
            if episode_end:
                episode = f"E{int(episode_start):02} to E{int(episode_end):02}"
            else:
                episode = f"{int(episode_start):02}"
            break
    # Year detection
    year_match = re.search(r'(?<!\d)((?:19|20)\d{2})(?!\d)', text)
    year = year_match.group(1) if year_match else None

    # Resolution detection
    quality_match = re.search(r'(480p|720p|1080p|2160p|4k)', text)
    resolution = quality_match.group(1).upper() if quality_match else None

    # Language detection
    languages_raw = re.findall(r'\b(?:' + '|'.join(LANG_MAP.keys()) + r')\b', text)
    languages = list({LANG_MAP.get(lang.lower(), lang.capitalize()) for lang in languages_raw})

    # Dual/Multi prefix formatting
    if "dual" in text:
        lang = f"dual - {', '.join(sorted(languages))}" if languages else "dual"
    elif "multi" in text:
        lang = f"multi - {', '.join(sorted(languages))}" if languages else "multi"
    else:
        lang = ', '.join(sorted(languages)) if languages else None

    return {
        "season": season,
        "episode": episode,
        "year": year,
        "resolution": resolution,
        "language": lang
    }
def extract_languages_and_year(caption_text: str, file_name: str):
    text = f"{caption_text or ''} {file_name}".lower()

    # Extract year (4 digit between 1900 and 2099)
    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    year = year_match.group(1) if year_match else "N/A"

    # Detect language codes and full names
    langs_found = set()
    for code, full in LANGUAGE_MAP.items():
        if re.search(rf'\b{code}\b', text) or re.search(rf'\b{full.lower()}\b', text):
            langs_found.add(full)

    langs_list = sorted(langs_found)
    lang_label = "N/A"
    if langs_list:
        if "Multi" in text:
            lang_label = f"Multi - {', '.join(langs_list)}"
        elif "Dual" in text or len(langs_list) == 2:
            lang_label = f"Dual - {', '.join(langs_list)}"
        else:
            lang_label = ", ".join(langs_list)

    return lang_label, year
    
def extract_from_filename(name):
    name_lower = name.lower()

    # Mapping short codes & language names
    lang_map = {
        "eng": "English", "english": "English",
        "hin": "Hindi", "hindi": "Hindi",
        "spa": "Spanish", "spanish": "Spanish",
        "tam": "Tamil", "tamil": "Tamil",
        "tel": "Telugu", "telugu": "Telugu",
        "mal": "Malayalam", "malayalam": "Malayalam",
        "kan": "Kannada", "kannada": "Kannada",
        "pun": "Punjabi", "punjabi": "Punjabi",
        "mar": "Marathi", "marathi": "Marathi",
        "guj": "Gujarati", "gujarati": "Gujarati",
        "jap": "Japanese", "japanese": "Japanese",
        "kor": "Korean", "korean": "Korean",
        "fre": "French", "french": "French",
        "ger": "German", "german": "German",
        "ita": "Italian", "italian": "Italian",
        "multi": "Multi", "dual": "Dual"
    }

    # Clean filename
    clean = re.sub(r"[(){}]", " ", name_lower)
    clean = re.sub(r"[^a-z0-9+]", " ", clean)

    # Year
    year_match = re.search(r"\b(19\d{2}|20\d{2})\b", name_lower)
    year = year_match.group(1) if year_match else "N/A"

    # Season
    season_match = re.search(r"s(\d{1,2})", name_lower)
    season = f"{int(season_match.group(1)):02d}" if season_match else "N/A"

    # Episode with range (like e01-05 or e01_05 or e01to05)
    ep_range_match = re.search(r"e(\d{2,4})\D*?(\d{2,4})", name_lower)
    if ep_range_match:
        episode = f"{ep_range_match.group(1)}–{ep_range_match.group(2)}"
    else:
        ep_match = re.search(r"e(\d{1,4})", name_lower)
        episode = f"{int(ep_match.group(1)):02d}" if ep_match else "N/A"

    # Quality
    quality_match = re.search(r"(144p|240p|360p|480p|720p|1080p|2160p|4k)", name_lower)
    quality = quality_match.group(1) if quality_match else "N/A"

    # Extension
    ext_match = re.search(r"\.([a-z0-9]{2,5})$", name)
    ext = ext_match.group(1) if ext_match else "N/A"

    # Language
    lang_found = []
    for code, full in lang_map.items():
        if re.search(rf"\b{re.escape(code)}\b", clean):
            if full not in lang_found:
                lang_found.append(full)

    if "Dual" in lang_found:
        lang_found.remove("Dual")
        language = f"Dual - {', '.join(lang_found)}" if lang_found else "Dual"
    elif "Multi" in lang_found:
        lang_found.remove("Multi")
        language = f"Multi - {', '.join(lang_found)}" if lang_found else "Multi"
    else:
        language = ", ".join(lang_found) if lang_found else "N/A"

    return {
        "year": year,
        "quality": quality,
        "season": season,
        "episode": episode,
        "language": language,
        "ext": ext
        }      
"""def extract_from_filename(name):
    name_lower = name.lower()

    # Extension (last dot-based split)
    ext = os.path.splitext(name)[1].lower().strip() or "N/A"
    patterns = {
        "year": r"\b(19\d{2}|20\d{2})\b",
        "quality": r"(144p|240p|360p|480p|720p|1080p|2160p|4k)",
        "season": r"(?:s|season)[\s._-]?(\d{1,2})",
        "episode": r"(?:e|episode)[\s._-]?(\d{1,4})"
    }

    results = {}
    for key, pat in patterns.items():
        match = re.search(pat, name_lower)
        results[key] = match.group(1) if match else "N/A"

    return {
        "year": results["year"],
        "quality": results["quality"],
        "season": results["season"],
        "episode": extract_episode_range(name),
        "language": extract_languages(name),
        "ext": ext
        }"""

def format_caption(template, file_name, file_size, caption="", duration=None, height=None, width=None, mime_type=None, media_type=None, title=None, artist=None):
    info = extract_from_filename(file_name)
    test = extract_metadata(file_name, caption)
    resolution = f"{width}x{height}" if width and height else "N/A"
    clean_name = clean_filename(file_name)
    lang, year = extract_languages_and_year(caption, clean_name)
    
    placeholders = {
        "{filename}": clean_name,
        "{filesize}": get_size(file_size),
        "{caption}": caption or "",
        "{language}": test["language"],
        "{year}": year,
        "{quality}": info["quality"],
        "{season}": test["season"],
        "{episode}": test["episode"],
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
    
