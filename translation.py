# (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import os

class TXT(object):

# ===================== [ START TEXT ] ===================== #

    START = """<b>Jᴀɪ Sʜʀᴇᴇ Kʀɪꜱʜɴᴀ...🙏🏻

ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ Aᴅᴠᴀɴᴄᴇ ꜰᴇᴀᴛᴜʀᴇꜱ !
I ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴꜱ ғᴏʀ ᴠɪᴅᴇᴏꜱ, ᴀᴜᴅɪᴏ ғɪʟᴇꜱ, ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴘᴏꜱᴛᴇᴅ ᴏɴ ᴄʜᴀɴɴᴇʟꜱ.</b>

<blockquote>⚠️ 𝐍𝐎𝐓𝐄: 𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 '𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒' & '𝐇𝐄𝐋𝐏' 𝐁𝐮𝐭𝐭𝐨𝐧 𝐭𝐨 𝐋𝐞𝐚𝐫𝐧 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 ⚠️</blockquote>"""

# ===================== [ HELP TEXT ] ===================== # 

    HELP = """<blockquote><b> ❗ 𝐑𝐞𝐚𝐝 𝐂𝐚𝐫𝐞𝐟𝐮𝐥𝐥𝐲 ❗ </b></blockquote>

<blockquote>• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪ ɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.
• Cʜᴇᴄᴋ Mᴀʀᴋᴅᴏᴡɴꜱ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Uꜱᴇ Tʜᴇᴍ</blockquote>

➣ <code>/setcap</code> or <code>/setcaption</code> - ᴛᴏ Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
➣ <code>/delcap</code> or <code>/delcaption</code> - ᴛᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ
➣ <code>/preview</code> or <code>/showcap</code> - ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ
➣ <code>/button</code> or <code>/setbutton</code> - ᴛᴏ ꜱᴇᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ғᴏʀ ɪɴᴄᴏᴍɪɴɢ ғɪʟᴇꜱ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
➣ <code>/delbutton</code> - ᴛᴏ ᴅɪꜱᴀʙʟᴇ/ᴅᴇʟᴇᴛᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
➣ <code>/variables</code> - ᴛᴏ ꜱᴇᴇ/ᴄʜᴇᴄᴋ ᴀʟʟ ᴠᴀʟɪᴅ ᴠᴀʀɪᴀʙʟᴇꜱ

𝑭𝒐𝒓𝒎𝒂𝒕:

Eg:- <code>/setcap 
<b>• Fɪʟᴇɴᴀᴍᴇ = {filename} 
• ꜱɪᴢᴇ = {filesize} 
• OTT = {ottprint}
• Lᴀɴɢ = {language} 
• Yᴇᴀʀ = {year} 
• Qᴜᴀʟɪᴛʏ= {quality} 
• Dᴜʀᴀᴛɪᴏɴ = {duration}

𝖩𝗈𝗂𝗇  ➥ 「 @Bots_Office 」</b></code>

<b>Aʟʟ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡᴏʀᴋꜱ ᴏɴ ᴄʜᴀɴɴᴇʟꜱ ᴏɴʟʏ ⚠</b>"""

# ===================== [ ABOUT TEXT ] ===================== #

    ABOUT = """<b>⍟──────[ 🔘 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 🔘 ]──────⍟

<blockquote>➣ ʙᴏᴛ : <a href='https://t.me/Public_Caption_Bot'>Pᴜʙʟɪᴄ Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ</a>
➣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/THE_DS_OFFICIAL'>ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️</a>
➣ Hᴏsᴛᴇᴅ ᴏɴ : Aɴʏᴡʜᴇʀᴇ 
➣ Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
➣ Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ
➣ ᴠᴇʀꜱɪᴏɴ : ᴠ𝟶.𝟹.𝟶</blockquote> 
⍟────[ @Public_Caption_Bot ]────⍟</b>"""


# ===================== [ MARKDOWN TEXT ] ===================== #


    MARKDOWN ="""<b>╔═❰ 🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧𝐬</u> 🔰 ❱══➣
║
║   <b>➢ ʙᴏʟᴅ ᴛᴇxᴛ</b>
║
║   ☞  <code>**{filename}**</code>      
║
║   <b>➢ ɪᴛᴀʟɪᴄ ᴛᴇxᴛ</b>
║
║   ☞ <code>__{filename}__</code>   
║
║   <b>➢ ɪɴʟɪɴᴇ ᴍᴏɴᴏ ᴛᴇxᴛ</b>
║
║   ☞ <code>`{filename}`</code>  
║
║   <b>➢ ʙʟᴏᴄᴋ ǫᴜᴏᴛᴇ ᴛᴇxᴛ</b>
║
║   ☞ <code> > {filename}</code>      
║
║   <b>➢ sᴛʀɪᴋᴇ ᴛʜʀᴏᴜɢʜ ᴛᴇxᴛ</b>
║
║   ☞ <code>~~{filename}~~</code>   
║ 
║   <b>➢ sᴘᴏɪʟᴇʀ ᴛᴇxᴛ</b>
║
║   ☞ <code>||{filename}||</code>   
║
║   <b>➢ ᴜɴᴅᴇʀʟɪɴᴇ ᴛᴇxᴛ</b>
║
║   ☞ <code><u>{filename}</u></code>
║  
║   <b>➢ ʜʏᴘᴇʀʟɪɴᴋ ᴛᴇxᴛ</b>
║
║   ☞ <code>[{filename}](https://t.me/Public_Caption_Bot)</code>
║
╚══════════════════➣""" 
    

# ===================== [ DONATE TEXT ] ===================== #


    DONATE = """<b>Hello Dear 👋🏻,

As you already know, this Advance Caption bot service is a free service. To run such a service, there are server expenses involved, I would really appreciate some  donation which will really help the service to be alive. Any amount is fine (10, 20, 30, 50, 100...) as long as you think the service deserves it. You can donate through UPI.</b>

<i><b>Thanks in advance, your contributions really matters.</b></i>
"""

# ===================== [ PRIVACY TEXT ] ===================== #


    PRIVACY = """<blockquote><b><u>Privacy Policy for Public Caption Bot ✨</u></b></blockquote>

Last updated: 15-05-2025

Thank you for using Public Caption Bot ! This Privacy Policy describes how your personal information is collected, used, and shared when you use this bot.

<blockquote><b><u>Information We Collect</u></b></blockquote>

Public Caption Bot collects user and channel IDs in order to ban users or channels that misuse the bot.

<blockquote><b><u><u>How We Use Your Information</u></b></blockquote>

We use user and channel IDs only to restrict access for users or channels that misuse the bot.

<blockquote><b><u>Sharing Your Information</u></b></blockquote>

We do not share any personal information with third parties.

<blockquote><b><u>Changes to This Privacy Policy</u></b></blockquote>

We may update this Privacy Policy from time to time in order to reflect, for example, changes to our practices or for other operational, legal, or regulatory reasons.

<blockquote><b><u>Contact</u></b></blockquote>

If you have any questions or suggestions about our Privacy Policy, Then Contact My Developer (see /start).</b>"""

    
# ===================== [ BOT VARIABLES ] ===================== #

    VAR = """<b>💥 ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴠᴀʀɪᴀʙʟᴇꜱ: 💥</b>
    
<b>⋗ Vɪᴅᴇᴏ/Dᴏᴄᴜᴍᴇɴᴛ Fɪʟʟɪɴɢs:</b>
• <code>{filename}</code> : ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{filesize}</code> : ᴏʀɪɢɪɴᴀʟ ғɪʟᴇ sɪᴢᴇ.
• <code>{caption}</code> : ғɪʟᴇ ᴄᴀᴘᴛɪᴏɴ.
• <code>{language}</code> : ʟᴀɴɢᴜᴀɢᴇs ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{year}</code> : ʏᴇᴀʀ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{quality}</code> : ǫᴜᴀʟɪᴛʏ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{ottprint}</code> : OTT ᴡɪᴛʜ ᴘʀɪɴᴛ.
• <code>{season}</code> : ꜱᴇᴀꜱᴏɴ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{episode}</code> : ᴇᴘɪꜱᴏᴅᴇ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{duration}</code> : ᴅᴜʀᴀᴛɪᴏɴ ғʀᴏᴍ ᴠɪᴅᴇᴏ ɪɴ Hᴏᴜʀ | Mɪɴ | Sᴇᴄ.
• <code>{height}</code> : ʜᴇɪɢʜᴛ ᴏғ ᴠɪᴅᴇᴏ.
• <code>{width}</code> : ᴡɪᴅᴛʜ ᴏғ ᴠɪᴅᴇᴏ.
• <code>{resolution}</code> : ʀᴇsᴏʟᴜᴛɪᴏɴ ᴏғ ᴠɪᴅᴇᴏ (ᴇɢ., 𝟷𝟿𝟸𝟶x𝟷𝟶𝟾𝟶).
• <code>{ext}</code> : ғɪʟᴇ ᴇxᴛᴇɴꜱɪᴏɴ (ᴍᴘ4, ᴍᴋᴠ, ᴇᴛᴄ.)
• <code>{mediatype}</code> : Tʏᴘᴇ ᴏғ ᴍᴇᴅɪᴀ (ᴇɢ., ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛ, ᴇᴛᴄ.)
• <code>{mimetype}</code> : ᴍɪᴍᴇ ᴛʏᴘᴇ ᴏғ ғɪʟᴇ.
• <code>{wish}</code> : ᴡɪꜱʜ (ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ, ᴇᴛᴄ.)

<b>⋗ Aᴜᴅɪᴏ Fɪʟʟɪɴɢs:</b>
• <code>{filename}</code> : ᴀᴜᴅɪᴏ ғɪʟᴇ ɴᴀᴍᴇ.
• <code>{filesize}</code> : ᴏʀɪɢɪɴᴀʟ ᴀᴜᴅɪᴏ ғɪʟᴇ sɪᴢᴇ.
• <code>{duration}</code> : ᴅᴜʀᴀᴛɪᴏɴ ғʀᴏᴍ ᴀᴜᴅɪᴏ ɪɴ Hᴏᴜʀ | Mɪɴ | Sᴇᴄ.
• <code>{ext}</code> : ᴀᴜᴅɪᴏ ғɪʟᴇ ᴇxᴛᴇɴꜱɪᴏɴ (ғʟᴀᴄ, ᴍᴘ𝟹, ᴇᴛᴄ.)
• <code>{mediatype}</code> : Tʏᴘᴇ ᴏғ ᴍᴇᴅɪᴀ (ᴇɢ., ᴀᴜᴅɪᴏ, ᴇᴛᴄ.)
• <code>{mimetype}</code> : ᴍɪᴍᴇ ᴛʏᴘᴇ ᴏғ ᴀᴜᴅɪᴏ ғɪʟᴇ.
• <code>{wish}</code> : ᴡɪꜱʜ (ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ, ᴇᴛᴄ.)
• <code>{title}</code> : ᴀᴜᴅɪᴏ ᴛɪᴛʟᴇ ɴᴀᴍᴇ.
• <code>{artist}</code> : ᴀᴜᴅɪᴏ ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ.

⚠️ <b>ɴᴏᴛᴇ: ᴅᴏɴᴛ ᴜsᴇ ᴀɴʏ ᴏᴛʜᴇʀ ᴠᴀʀɪᴀʙʟᴇ</b> ⚠️
"""

# ===================== [ HOW TO USE CMD ] ===================== #

    HTU_TXT = """<u>𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</u> ❓
    
<b>• Cʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.</b>    
"""
    
# ===================== [ SHOWCAP CMD ] ===================== #

    SHOWCAP = """<blockquote>𝐒𝐡𝐨𝐰𝐜𝐚𝐩 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🔥</blockquote>

<b>• ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ <code>/showcap</code> ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀ 'ᴄʜᴀɴɴᴇʟ', ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇᴛᴜʀɴ ᴛʜᴇ ꜱᴀᴠᴇᴅ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.

⚠️ ꜱᴇᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢ ⚠️</b>
"""

# ===================== [ SETCAP CMD ] ===================== #

    SETCAP = """<blockquote>𝐒𝐞𝐭𝐜𝐚𝐩𝐭𝐢𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🔥</blockquote>
    
<b>• ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ <code>/setcap</code> ᴏʀ <code>/setcaption</code> ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀ 'ᴄʜᴀɴɴᴇʟ', ʏᴏᴜ ᴄᴀɴ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.

<blockquote>➢ Yᴏᴜ ᴄᴀɴ ᴜꜱᴇ HTML ᴍᴀʀᴋᴅᴏᴡɴ ɪɴ ʏᴏᴜʀ ᴛᴇᴍᴘʟᴀᴛᴇ. (ɢɪᴠᴇ ᴛʜᴇ /start ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ "Mᴀʀᴋᴅᴏᴡɴ" ʙᴜᴛᴛᴏɴ ᴛᴏ ꜱᴇᴇ ᴀʟʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴀʀᴋᴅᴏᴡɴꜱ.)

➢ Cʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴠᴀʀɪᴀʙʟᴇꜱ/ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀꜱ, ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴏɴᴇꜱ ʏᴏᴜ ɴᴇᴇᴅ, ᴀɴᴅ ꜱᴇɴᴅ ʏᴏᴜʀ ᴛᴇᴍᴘʟᴀᴛᴇ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴜꜱɪɴɢ ᴛʜᴇ <code>/setcap</code> ᴄᴏᴍᴍᴀɴᴅ.</blockquote>

Example:
<code>/setcap
<b>• Filename = {filename}
• Size = {filesize}
• OTT = {ottprint}
• Language = {language}
• Year = {year}
• Quality = {quality}
• Duration = {duration}

Join ➥ 「 @Bots_Office 」</b></code>

⚠️ ꜱᴇᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢ ⚠️</b>
"""

# ===================== [ DELCAP CMD ] ===================== #

    DELCAP = """<blockquote>𝐃𝐞𝐥𝐜𝐚𝐩𝐭𝐢𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🔥</blockquote>
    
<b>• ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ <code>/delcap</code> ᴏʀ <code>/delcaption</code> ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀ 'ᴄʜᴀɴɴᴇʟ', ʏᴏᴜ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ᴀɴᴅ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴛ ᴄʜᴀɴɢᴇ ᴄᴀᴘᴛɪᴏɴ ᴏғ ɴᴇᴡ ғɪʟᴇꜱ.

⚠️ ꜱᴇᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢ ⚠️</b>
"""    

# ===================== [ SETBUTTON CMD ] ===================== #

    SETBUTTON = """<blockquote>𝐒𝐞𝐭𝐛𝐮𝐭𝐭𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🔥</blockquote>

<b>• ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ <code>/setbutton</code> ᴄᴏᴍᴍᴀɴᴅ ʙʏ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ɪɴ ᴀ 'ᴄʜᴀɴɴᴇʟ', ʏᴏᴜ ᴄᴀɴ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.

➢ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴛ ʏᴏᴜʀ ʙᴜᴛᴛᴏɴ ɪɴ ᴏɴᴇ ʀᴏᴡ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ʀᴏᴡ
➢ Dᴏɴ'ᴛ ʟᴇᴀᴠᴇ ᴀɴʏ ᴇxᴛʀᴀ ᴡʜɪᴛᴇꜱᴘᴀᴄᴇ ⚠️ 
➢ ʙʏ ᴜꜱɪɴɢ '<code>|</code>' ᴛʜɪꜱ ᴋᴇʏᴡᴏʀᴅ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪᴘʟᴇ ʙᴜᴛᴛᴏɴꜱ 
➢ Sʏɴᴛᴀx ɪꜱ /setbutton ʙᴜᴛᴛᴏɴ_ᴛᴇxᴛ = ʙᴜᴛᴛᴏɴ_ᴜʀʟ

☞ Example𝟷 : (Fᴏʀ 𝟸 ʙᴜᴛᴛᴏɴ ɪɴ 𝟷 ʀᴏᴡ)
<code>/setbutton Watch Now = https://example.com | Visit Site = https://anotherexample.com</code>

☞ Example𝟸 : (Fᴏʀ 𝟸 ʙᴜᴛᴛᴏɴ ɪɴ 𝟸 ʀᴏᴡ)
<code>/setbutton Watch Now = https://example.com
Visit Site = https://anotherexample.com</code>

⚠️ ꜱᴇᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢ ⚠️</b>    
"""

# ===================== [ DELBUTTON CMD ] ===================== #

    DELBUTTON = """<blockquote>𝐃𝐞𝐥𝐛𝐮𝐭𝐭𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🔥</blockquote>

<b>• ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ <code>/delbutton</code> ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀ 'ᴄʜᴀɴɴᴇʟ', ʏᴏᴜ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.

⚠️ ꜱᴇᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢ ⚠️</b>    
"""

# ===================== [😎 THE END 😎] ===================== #
