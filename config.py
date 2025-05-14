# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

# ===================== [ Config Variable Class ] ===================== #

class DS(object):
    
    # Bot config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "25833520")
    API_HASH = os.environ.get("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7016777070:AAFlFW1ELdwUP36MV0zCyy43Dlv9iHSz5HI")

    # start_pic
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/lCm.jpg") 
    
    # caption help image
    SETCAP_PIC = os.environ.get("SETCAP_PIC", "https://freeimage.host/i/3UcBqQI")
    DELCAP_PIC = os.environ.get("DELCAP_PIC", "https://envs.sh/oQk.jpg")
    SHOWCAP_PIC = os.environ.get("SHOWCAP_PIC", "https://envs.sh/oiD.jpg")
    SETBUTTON_PIC = os.environ.get("SETBUTTON_PIC", "https://envs.sh/oeU.jpg")
    DELBUTTON_PIC = os.environ.get("DELBUTTON_PIC", "https://envs.sh/oQl.jpg")

    # upi id qr code image
    UPI_QR_PIC = os.environ.get("UPI_QR_CODE", "https://envs.sh/l9M.jpg")

    # markdown Image
    MARKDOWN_PIC = os.environ.get("MARKDOWN_PIC", "https://envs.sh/l9U.jpg")
    
    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002263150627"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002263150627"))  # Replace with your log channel ID
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "pubcapbot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b>{caption}</b>",
    )

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1562935405').split()]


# ===================== [ THE END ] ===================== #

