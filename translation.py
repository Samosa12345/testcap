# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import os

class TXT(object):

# ===================== [ START TEXT ] ===================== #

    START = """<b>Jᴀɪ Sʜʀᴇᴇ Kʀɪꜱʜɴᴀ...🙏🏻

ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ Aᴅᴠᴀɴᴄᴇ ꜰᴇᴀᴛᴜʀᴇꜱ !
I ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴꜱ ғᴏʀ ᴠɪᴅᴇᴏꜱ, ᴀᴜᴅɪᴏ ғɪʟᴇꜱ, ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴘᴏꜱᴛᴇᴅ ᴏɴ ᴄʜᴀɴɴᴇʟꜱ.

<blockquote>ᴜꜱᴇ /setcap ᴛᴏ ꜱᴇᴛ ᴄᴀᴘᴛɪᴏɴ\nᴜꜱᴇ /delcap Tᴏ ᴅᴇʟᴇᴛᴇ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ꜱᴇᴛ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴅᴇғᴀᴜʟᴛ.</blockquote>

Nᴏᴛᴇ: Cᴀᴘᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡᴏʀᴋꜱ ᴏɴ ᴄʜᴀɴɴᴇʟꜱ ᴏɴʟʏ ⚠</b>"""

# ===================== [ HELP TEXT ] ===================== # 

    HELP = """<blockquote><b> ❗ 𝐑𝐞𝐚𝐝 𝐂𝐚𝐫𝐞𝐟𝐮𝐥𝐥𝐲 ❗ </b></blockquote>

<blockquote>• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.
• Cʜᴇᴄᴋ Mᴀʀᴋᴅᴏᴡɴꜱ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Uꜱᴇ Tʜᴇᴍ</blockquote>

➣ /setcap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
➣ /delcap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ

𝑭𝒐𝒓𝒎𝒂𝒕:

<code>{file_name}</code> = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
<code>{post_caption}</code> = Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ
<code>{file_size}</code> = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 

Eg:- <code>/setcap 
{file_name} / {post_caption}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
🔸 𝐉𝐨𝐢𝐧 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
🔸 𝐉𝐨𝐢𝐧 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</code>"""

# ===================== [ ABOUT TEXT ] ===================== #

    ABOUT = """<b>⍟────[ 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ]────⍟

<blockquote>➣ 📃ʙᴏᴛ : <a href='https://t.me/Public_Caption_Bot'>Pᴜʙʟɪᴄ Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ</a>
➣ 👦Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/THE_DS_OFFICIAL'>ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️</a>
➣ 🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/Silent_Bots'>Sɪʟᴇɴᴛ Bᴏᴛꜱ</a>
➣ 📡Hᴏsᴛᴇᴅ ᴏɴ : Aɴʏᴡʜᴇʀᴇ 
➣ 🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
➣ 📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ
➣ 👨🏻‍💻Cʀᴇᴅɪᴛꜱ : @THE_DS_OFFICIAL & @Biisal</blockquote> 
⍟────[ @Public_Caption_Bot ]────⍟</b>"""


# ===================== [ MARKDOWN TEXT ] ===================== #


    MARKDOWN ="""🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧𝐬</u> 🔰

💡 <b>Bold text</b>
  <code>**{file_name}**</code> 𝐨𝐫 <code><b>{file_name}</b></code>

💡 <b>Italic text</b>
  <code>__{post_caption}__</code> 𝐨𝐫 <code><i>{post_caption}</i></code>

💡 <b>Code text</b>
  <code>`{file_size}`</code> 𝐨𝐫 <code><code>{file_size}</code></code>  

💡 <b>Quote Text</b>
  <code> > {file_name}</code> 𝐨𝐫 <code><blockquote>{file_size}</blockquote></code>  

💡 <b>Underline Text</b>
  <code><u>{post_caption}</u></code>

💡 <b>Strike Text</b>
  <code>~~{file_size}~~</code> 𝐨𝐫 <code><s>{file_size}</s></code>

💡 <b>Spoiler Text</b>
  <code>||{file_name}||</code> 𝐨𝐫 <code><spoiler>{file_name}</spoiler></code>

💡 <b>Hyperlink text</b>
  <code>[{post_caption}](https://t.me/Public_Caption_Bot)</code>""" 
    

# ===================== [ DONATE TEXT ] ===================== #


    DONATE = """<b>Hello Dear 👋🏻,

As you already know, this Advance Caption bot service is a free 
service. To run such a service, there are server expenses involved, I 
would really appreciate some  donation which will really help the 
service to be alive. Any amount is fine (10, 20, 30, 50, 100...) as long 
as you think the service deserves it. You can donate through UPI ID 
or Scan this QRCode.</b>

<i><b>Thanks in advance, your contributions really matters.</b></i>
"""

# ===================== [ PRIVACY TEXT ] ===================== #


    PRIVACY = """<blockquote><b><u>Privacy Policy for Public Caption Bot</u></b></blockquote>

Last updated: 15-08-2024

Thank you for using Public Caption Bot ! This Privacy Policy 
describes how your personal information is collected, used, 
and shared when you use this bot.

<blockquote><b><u>Information We Collect</u></b></blockquote>

Public Caption Bot does not collect any personal information 
from its users.

<blockquote><b><u><u>How We Use Your Information</u></b></blockquote>

Since we do not collect any personal information, we do not use, 
store, or share any information about you.

<blockquote><b><u>Sharing Your Information</u></b></blockquote>

We do not share any personal information because we do not collect 
any personal information.

<blockquote><b><u>Changes to This Privacy Policy</u></b></blockquote>

We may update this Privacy Policy from time to time in order to 
reflect, for example, changes to our practices or for other 
operational, legal, or regulatory reasons.

<blockquote><b><u>Contact</u></b></blockquote>

If you have any questions or suggestions about our Privacy Policy, 
Then Contact My Developer (see /start).</b>
"""


# ===================== [ BOT LIST TEXT ] ===================== #


    BOTLIST = """<blockquote>🔥 <u>𝐒𝐢𝐥𝐞𝐧𝐭 𝐏𝐮𝐛𝐥𝐢𝐜 𝐁𝐨𝐭 𝐋𝐢𝐬𝐭</u> 🔥</blockquote>

<blockquote>1. <b>Public File Store Bot</b> ⚡
    👉🏻 @PublicFileStore01_Bot</blockquote>
    
    You Can Save Your Files, Videos, Photos etc On Bot,
    and get anywhere, anytime when you want !

<blockquote>2. <b>Public File To Link / Stream Bot</b> ⚡
    👉🏻 @PublicFileToLink01Bot</blockquote>

    You Can Generate Fast Download link & Stream Link 
    Stream Videos On Internet (Without Downloading)
    Group Support Added !

<blockquote>3. <b>Public Auto Reaction Bot</b> ⚡
    👉🏻 @SILENT_REACT_BOT</blockquote>

    This Bot Will Give Reaction On Your Message !
    Support In Group & Channel Both ! 

<blockquote>4. <b>Public Caption Bot Beta</b> ⚡
    👉🏻 @PublicCaption_Bot</blockquote>

    This bot is Beta Version Of Advance Caption Bot !
    Easy To Use !
    This Bot have Simple UI & Caption System  

<blockquote>5. <b>Advance Public Caption Bot</b> ⚡
    👉🏻 @Public_Caption_Bot</blockquote>

    This is an advance and Multifunctional caption bot !
    caption with file_name & post_caption & file_size Supported

<blockquote>6. <b>Public Instagram Downloader Bot</b> ⚡</blockquote>
    👉🏻 Bot is Under maintaince
    
<blockquote>7. <b>Public Spotify Music Downloader Bot</b></blockquote>
    👉🏻 Bot is Under maintaince"""


# ===================== [😎 END OF translation.py 😎] ===================== #
