# (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import os

class TXT(object):

# ===================== [ START TEXT ] ===================== #

    START = """<b>Jᴀɪ Sʜʀᴇᴇ Kʀɪꜱʜɴᴀ...🙏🏻

ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ Aᴅᴠᴀɴᴄᴇ ꜰᴇᴀᴛᴜʀᴇꜱ !
I ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴꜱ ғᴏʀ ᴠɪᴅᴇᴏꜱ, ᴀᴜᴅɪᴏ ғɪʟᴇꜱ, ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴘᴏꜱᴛᴇᴅ ᴏɴ ᴄʜᴀɴɴᴇʟꜱ.</b>

<blockquote>𝐍𝐎𝐓𝐄: 𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 '𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒' & '𝐇𝐄𝐋𝐏' 𝐁𝐮𝐭𝐭𝐨𝐧 𝐭𝐨 𝐋𝐞𝐚𝐫𝐧 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭</blockquote>"""

# ===================== [ HELP TEXT ] ===================== # 

    HELP = """<blockquote><b> ❗ 𝐑𝐞𝐚𝐝 𝐂𝐚𝐫𝐞𝐟𝐮𝐥𝐥𝐲 ❗ </b></blockquote>

<blockquote>• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪ ɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.
• Cʜᴇᴄᴋ Mᴀʀᴋᴅᴏᴡɴꜱ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Uꜱᴇ Tʜᴇᴍ</blockquote>

➣ /setcap or /setcaption- ᴛᴏ Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
➣ /delcap or /delcaption - ᴛᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ
➣ /preview or /showcap - ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ
➣ /button or /setbutton - ᴛᴏ ꜱᴇᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ғᴏʀ ɪɴᴄᴏᴍɪɴɢ ғɪʟᴇꜱ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
➣ /delbutton - ᴛᴏ ᴅɪꜱᴀʙʟᴇ/ᴅᴇʟᴇᴛᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
➣ /variables - ᴛᴏ ꜱᴇᴇ/ᴄʜᴇᴄᴋ ᴀʟʟ ᴠᴀʟɪᴅ ᴠᴀʀɪᴀʙʟᴇꜱ

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
➣ Cʀᴇᴅɪᴛꜱ : @THE_DS_OFFICIAL</blockquote> 
⍟────[ @Public_Caption_Bot ]────⍟</b>"""


# ===================== [ MARKDOWN TEXT ] ===================== #


    MARKDOWN ="""<b>╔═❰ 🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧𝐬</u> 🔰 ❱══➣
║
║   <b>➢ ʙᴏʟᴅ ᴛᴇxᴛ</b>
║
║   ☞  <code>**{filename}**</code>   
║   ☞  <code><b>{filename}</b></code>   
║
║   <b>➢ ɪᴛᴀʟɪᴄ ᴛᴇxᴛ</b>
║
║   ☞ <code>__{filename}__</code>   
║   ☞ <code><i>{filename}</i></code>  
║   ☞ <code><em>{filename}</em></code>
║    
║   <b>➢ ɪɴʟɪɴᴇ ᴍᴏɴᴏ ᴛᴇxᴛ</b>
║
║   ☞ <code>`{filename}`</code> 
║   ☞ <code><code>{filename}</code></code>
║ 
║   <b>➢ ᴍᴜʟᴛɪʟɪɴᴇ ᴄᴏᴅᴇ ʙʟᴏᴄᴋ</b>
║
║   ☞ <code><pre>{filename}</pre></code>
║
║   <b>➢ ʙʟᴏᴄᴋ ǫᴜᴏᴛᴇ ᴛᴇxᴛ</b>
║
║   ☞ <code> > {filename}</code>   
║   ☞ <code><blockquote>{filename}</blockquote></code>   
║
║   <b>➢ sᴛʀɪᴋᴇ ᴛʜʀᴏᴜɢʜ ᴛᴇxᴛ</b>
║
║   ☞ <code>~~{filename}~~</code>   
║   ☞ <code><s>{filename}</s></code>  
║   ☞ <code><del>{filename}</del></code>
║ 
║   <b>➢ sᴘᴏɪʟᴇʀ ᴛᴇxᴛ</b>
║
║   ☞ <code>||{filename}||</code>   
║   ☞ <code><spoiler>{filename}</spoiler></code>
║
║   <b>➢ ᴜɴᴅᴇʀʟɪɴᴇ ᴛᴇxᴛ</b>
║
║   ☞ <code><u>{filename}</u></code>
║  
║   <b>➢ ʜʏᴘᴇʀʟɪɴᴋ ᴛᴇxᴛ</b>
║
║   ☞ <code>[{filename}](https://t.me/Public_Caption_Bot)</code>
║   ☞ <code><a href="https://t.me/Public_Caption_Bot">{filename}</a></code>
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
• <code>{ottprint}</code> : OTT ᴡɪᴛʜ ᴘʀɪɴᴛ (ᴇɢ. Zᴇᴇ𝟻 - WEBRɪᴘ).
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
    
# ===================== [😎 END OF translation.py 😎] ===================== #
