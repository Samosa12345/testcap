# (c) @Bisal & (c) @Sanchit0102

import os, re, asyncio
from datetime import datetime
from zoneinfo import ZoneInfo  
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .database import *
from config import DS
from translation import TXT 

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

PRINTS = {
    "bluray": "Bluray", "brrip": "BR-Rip", "bdrip": "BD-Rip",
    "web-dl": "WEB-DL", "webdl": "WEB-DL", "webrip": "WEBRip", "web-rip": "WEBRip",
    "hdrip": "HDRip", "dvdrip": "DVD-Rip", "hdtvdl": "HDTV-DL", "hdtv": "HDTV",
    "tvrip": "TVRip", "hd-tvrip": "HDTV-Rip", "pdtv": "PDTV", "sdtv": "SDTV",
    "uhd": "UHD", "hdts": "HDTS", "hdtc": "HDTC", "ytdl": "YTDL",
    "hdcam": "HDCAM", "hdcamrip": "HDCAM-Rip", "hq s-print": "HQ S-Print",
    "camrip": "HDCAM-Rip", "telesync": "TELESYNC", "dvdscr": "DVD-SCR",
    "workprint": "WORK PRINT", "repack": "REPACK", "extended": "EXTENDED", "unrated": "UNRATED"
}

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
    await message.reply(TXT.VAR)
    
# /button command to save buttons (channel only)
@Client.on_message(filters.command("button") & filters.channel)
async def set_buttons(bot, message):
    if not message.reply_to_message:
        return await message.reply("Please reply to a media message and provide button data.")

    raw = message.text.split(None, 1)
    if len(raw) < 2:
        return await message.reply("No button format found.")

    buttons = await parse_buttons(raw[1])
    if not buttons:
        return await message.reply("Invalid button format.")

    await set_channel_buttons(message.chat.id, buttons)
    await message.reply("Buttons saved for this channel!")

# /delbutton to remove buttons
@Client.on_message(filters.command("delbutton") & filters.channel)
async def del_buttons(bot, message):
    await buttons_col.delete_one({"channel_id": message.chat.id})
    await message.reply("Buttons deleted for this channel.")

def get_wish():
    time = datetime.now(ZoneInfo("Asia/Kolkata"))
    hour = time.hour
    if 5 <= hour < 12:
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
        
def extract_metadata(name: str, caption: str = "") -> dict:
    normalized_text = f"{name} {caption}".lower()
    text = normalized_text.replace('-', ' ').replace('.', ' ')

    pattern = r'(?<!\w)(' + '|'.join(map(re.escape, PRINTS.keys())) + r')(?!\w)'
    print_raw = re.findall(pattern, normalized_text)
    printf = list(dict.fromkeys(PRINTS.get(pf) for pf in print_raw if pf))

    # OTT detection
    ott_keys = {
        "nf": "NETFLIX", "hotstar": "Hotstar", "amzn": "AMZN", "jh": "Jio-Hotstar", "hulu": "HULU", "hbo": "HBO MAX",
        "zee5": "ZEE5", "sonyliv": "SONYLIV", "sony liv": "SONYLIV", "crunchyroll": "Crunchyroll", "cr": "Crunchyroll",
        "voot": "VOOT", "paramount": "PARAMOUNT", "peacock": "PEACOCK", "jc": "JIO CINEMA", "jio": "Jio Cinema",
        "mubi": "MUBI", "jio cinema": "JIO CINEMA", "jiocinema": "JIO CINEMA", "aha": "AHA", "altbalaji": "ALT BALAJI",
        "amc": "AMC+", "alt": "ALT BALAJI", "mx": "MX", "mx player": "MX", "sun nxt": "SUN NXT", "sunnxt": "SUN NXT",
        "apple tv": "Apple TV+", "discovery": "DISCOVERY", "eros": "EROS NOW", "eros now": "EROS NOW", "ujhs": "Ultra Jhakaas",
        "ultra jhakaas": "Ultra Jhakaas", "ultra play": "Ultra Play", "youtube": "YOUTUBE", "lionsgate play": "Lionsgate Play",
        "lionsgate": "Lionsgate Play", "starz": "STARZ", "chorki": "Chorki"
    }

    ott_name = "" #if not working then use None
    for key, label in ott_keys.items():
        if key in normalized_text:
            ott_name = label
            break
            
    if ott_name and printf:
        p = f"{ott_name} - {', '.join(sorted(printf))}"
    elif ott_name:
        p = ott_name
    elif printf:
        p = ', '.join(sorted(printf))
    else:
        p = "N/A"
        
    season_match = re.search(r'(?:s|season)[\s\._-]*(\d+)', text, re.IGNORECASE)
    season = season_match.group(1) if season_match else "N/A"
    
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
    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    year = year_match.group(1) if year_match else "N/A"

    # Resolution detection
    quality_match = re.search(r"(144p|240p|360p|480p|720p|1080p|2160p|4k)", text)
    quality = quality_match.group(1) if quality_match else "N/A"

    ext_match = re.search(r"\.([a-z0-9]{2,5})$", name)
    ext = ext_match.group(1) if ext_match else "N/A"
    
    # Language detection
    languages_raw = re.findall(r'\b(?:' + '|'.join(LANG_MAP.keys()) + r')\b', text)
    languages = list({LANG_MAP.get(lang.lower(), lang.capitalize()) for lang in languages_raw})

    # Dual/Multi prefix formatting
    if "dual" in text:
        lang = f"Dual - {', '.join(sorted(languages))}" if languages else "Dual"
    elif "multi" in text:
        lang = f"Multi - {', '.join(sorted(languages))}" if languages else "Multi"
    else:
        lang = ', '.join(sorted(languages)) if languages else "N/A"

    return {
        "prints": p,
        "quality": quality,
        "extension": ext,
        "season": season,
        "episode": episode,
        "year": year,
        "language": lang
    }

# Parse buttons from raw text (without callback data)
async def parse_buttons(raw_text):
    buttons = []
    rows = raw_text.strip().split('\n')
    for row in rows:
        line = []
        for button in row.strip().split('|'):
            try:
                if '=' in button:
                    text, url = button.strip().split('=')
                    line.append(InlineKeyboardButton(text=text.strip(), url=url.strip()))
            except Exception:
                continue
        if line:
            buttons.append(line)
    return buttons
    
def format_caption(template, file_name, file_size, caption="", duration=None, height=None, width=None, mime_type=None, media_type=None, title=None, artist=None):
    info = extract_metadata(file_name, caption)
    resolution = f"{width}x{height}" if width and height else "N/A"
    
    placeholders = {
        "{filename}": clean_filename(file_name),
        "{filesize}": get_size(file_size),
        "{caption}": caption or "",
        "{language}": info["language"],
        "{year}": info["year"],
        "{quality}": info["quality"],
        "{season}": info["season"],
        "{episode}": info["episode"],
        "{ott_print}": info["prints"],
        "{duration}": format_duration(duration),
        "{height}": str(height or "N/A"),
        "{width}": str(width or "N/A"),
        "{resolution}": resolution,
        "{ext}": info["extension"],
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
    else:
        await message.copy(DS.LOG_CHANNEL)

    # Check if channel is not banned
    if not await is_channel_banned(chnl_id):
        try:
            invite_link = await bot.export_chat_invite_link(chnl_id)
        except ChatAdminRequired:
            invite_link = "Invite link not available"

        try:
            members = await bot.get_chat_members_count(chnl_id)
        except Exception:
            members = "Unknown"

        await bot.send_message(
            DS.LOG_CHANNEL,
            f"#NewChannel\n\n"
            f"Title: <b>{message.chat.title}</b>\n"
            f"ID: <code>{chnl_id}</code>\n"
            f"Members: {members}\n"
            f"Invite: {invite_link}"
        )

        # Re-check in case ban was applied recently
        if await is_channel_banned(chnl_id):
            await message.reply("This channel is banned from using the bot. Contact the owner to unban.\n\n👀 Owner: @THE_DS_OFFICIAL")
            return

    default_caption = message.caption or ""
    cap_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    template = cap_data["caption"] if cap_data else DS.DEF_CAP.format(caption=clean_filename(default_caption))

    # Format the new caption
    new_caption = format_caption(
        template,
        file_name=file.file_name,
        file_size=file.file_size,
        caption=default_caption,
        duration=getattr(file, "duration", None),
        height=getattr(file, "height", None),
        width=getattr(file, "width", None),
        mime_type=getattr(file, "mime_type", None),
        media_type="Document" if message.document else "Video" if message.video else "Audio",
        title=getattr(file, "title", None),
        artist=getattr(file, "performer", None)
    )

    # Fetch inline buttons from DB
    buttons = await get_channel_buttons(chnl_id)
    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None

    try:
        await message.edit(new_caption, reply_markup=reply_markup)
    except Exception as e:
        print(f"Edit failed: {e}")
        
