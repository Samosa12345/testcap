# (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import os, re
from .database import * 
from datetime import datetime
from zoneinfo import ZoneInfo  
from pyrogram.types import InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

# ===================== [ GLOBLE VARIABLES ] ===================== #

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

# ===================== [ WISH FUNCTION ] ===================== #

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

# ===================== [ GET SIZE FUNCTION ] ===================== #

def get_size(size_bytes):
    size = float(size_bytes)
    for unit in ["Bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

# ===================== [ CLEAN FILENAME FUNCTION ] ===================== #

def clean_filename(name):
    name_without_ext = os.path.splitext(name)[0]
    clean = (re.sub(r'@\w+\s*', '', name_without_ext).replace("_", " ").replace(".", " ").replace("[", "").replace("]", "")).strip()  
    return f"{clean}{os.path.splitext(name)[1]}"

# ===================== [ CLEAN CAPTION FUNCTION ] ===================== #

async def clean_caption(chat_id, text):
    words = await get_removal_words(chat_id)
    for w in words:
        text = text.replace(w, "")
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'@\w+', '', text)     # remove mentions
    text = text.replace("_", " ").replace(".", " ").replace("[", "").replace("]", "")
    return text.strip()

# ===================== [ FORMAT FILE DURATION ] ===================== #

def format_duration(seconds):
    if not seconds:
        return "N/A"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{int(hours):02d}h {int(minutes):02d}m {int(sec):02d}s"

# ===================== [ EXTRACT DATA FROM FILENAME ] ===================== #

def extract_metadata(name: str, caption: str = "") -> dict:
    normalized_text = f"{name} {caption}".lower()
    text = normalized_text.replace('-', ' ').replace('.', ' ')

    pattern = r'(?<!\w)(' + '|'.join(map(re.escape, PRINTS.keys())) + r')(?!\w)'
    print_raw = re.findall(pattern, normalized_text)
    printf = list(dict.fromkeys(PRINTS.get(pf) for pf in print_raw if pf))

    # OTT detection
    ott_keys = {
        "nf": "NETFLIX", "hotstar": "Hotstar", "amzn": "AMZN", "jh": "Jio-Hotstar", "hulu": "HULU", "hbo": "HBO MAX",
        "zee5": "ZEE5", "sonyliv": "SONYLIV", "sliv": "SONYLIV", "sony liv": "SONYLIV", "crunchyroll": "Crunchyroll", "cr": "Crunchyroll",
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

# ===================== [ MAKE INLINE BUTTONS ] ===================== #
  
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

# ===================== [ MAKE TEMPLATE OF CAPTION FUNCTION ] ===================== #

def format_caption(template, filename, filesize, caption="", duration=None, height=None, width=None, mimetype=None, mediatype=None, title=None, artist=None):
    info = extract_metadata(filename, caption)
    resolution = f"{width}x{height}" if width and height else "N/A"
    
    placeholders = {
        "{filename}": clean_filename(filename),
        "{filesize}": get_size(filesize),
        "{caption}": caption or "",
        "{language}": info["language"],
        "{year}": info["year"],
        "{quality}": info["quality"],
        "{season}": info["season"],
        "{episode}": info["episode"],
        "{ottprint}": info["prints"],
        "{duration}": format_duration(duration),
        "{height}": str(height or "N/A"),
        "{width}": str(width or "N/A"),
        "{resolution}": resolution,
        "{ext}": info["extension"],
        "{mimetype}": mimetype or "N/A",
        "{mediatype}": mediatype or "N/A",
        "{title}": title or "N/A",
        "{artist}": artist or "N/A",
        "{wish}": get_wish()
    }

    for key, val in placeholders.items():
        template = template.replace(key, str(val))
    return template

# ===================== [ BAN CHANNEL MSG TO LOG CHANNEL ] ===================== #

async def log_channel_info(client, channel_id, text):
    try:
        chat = await client.get_chat(channel_id)
        title = chat.title or "Unknown"
        chat_id = chat.id

        try:
            members = await client.get_chat_members_count(channel_id)
        except Exception:
            members = "Unknown"

        try:
            invite_link = await client.export_chat_invite_link(channel_id)
        except ChatAdminRequired:
            invite_link = "❌ Bot is not admin, can't get invite link"

        message = (
            f"🔔 {text}\n\n"
            f"📢 <b>Title:</b> {title}\n"
            f"🆔 <b>ID:</b> <code>{chat_id}</code>\n"
            f"👥 <b>Members:</b> {members}\n"
            f"🔗 <b>Invite Link:</b> {invite_link}"
        )

        await client.send_message(DS.LOG_CHANNEL, message)
    except Exception as e:
        await client.send_message(DS.LOG_CHANNEL, f"⚠️ Failed to log channel info:\n{e}")


# ===================== [ THE END ] ===================== #
