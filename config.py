# (c) @Bisal & (c) @Sanchit0102

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class DS(object):
    
    # Bot config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "25833520")
    API_HASH = os.environ.get("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7312480511:AAF2V4w27h5IVZM9VbC-PAouV_UpSBCQKmA")

    # start_pic
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/c5952790fa8235f499749.jpg")

    # UPI QR Code Pic
    UPI_QR_CODE = os.environ.get("UPI_QR_CODE", "https://graph.org/file/7b782be88a32be378790f.jpg")

    # markdown Image
    MARKDOWN_PIC = os.environ.get("MARKDOWN_PIC", "https://envs.sh/ZEt.png")
    
    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = int(os.environ.get("FORCE_SUB", -1002104350566) )
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "testpubcapbot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b>{file_name}</b>",
    )

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1562935405').split()]
    
