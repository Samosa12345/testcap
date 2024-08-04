# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #


import os
from config import DS
import asyncio, time, sys
from .Force_Sub import checkSub
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, errors, enums
from .database import total_user, getid, delete, insert
from .buttons import BTN
from translation import TXT


# ===================== [ Incoming Txt Command ] ===================== #

EMOJI1 = "🤔"

# @Client.on_message(filters.private & filters.incoming)
async def capBot(bot, message):
    # await message.react(emoji=EMOJI1, big=True)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_text("use /start command to get started.")


# ===================== [ Start Command ] ===================== #

EMOJI2 = "😘"

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    # await message.react(emoji=EMOJI2, big=True)
    user_id = int(message.from_user.id)
    await insert(user_id)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.START_PIC,
        caption=TXT.START,  #f"<b>Hello, {message.from_user.mention} 👋🏻\n\nI'm an auto-caption bot. I automatically edit captions for videos, audio files, and documents posted on channels.\n\nuse <code>/set_caption</code> to set caption\nUse<code>/delcaption</code> To delete caption and set caption to default.\n\nNote:All commands works on channels only</b>",
        reply_markup=BTN.START_BTN 
    )

# ===================== [ Help Command ] ===================== #

EMOJI3 = "😉"

@Client.on_message(filters.private & filters.command(["help"]))
async def help(bot, message):
    await message.react(emoji=EMOJI3, big=True)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.START_IMG,
        caption=TXT.HELP,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.HELP_BTN
    )

# ===================== [ About Command ] ===================== #

EMOJI4 = "😎"

@Client.on_message(filters.private & filters.command(["about"]))
async def about(bot, message):
    await message.react(emoji=EMOJI4, big=True)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    # await message.reply_photo(
    await message.reply_text(
        # photo=DS.START_IMG,
        text=TXT.ABOUT,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.ABOUT_BTN,
        disable_web_page_preview=True 
    )


# ===================== [ Donate Command ] ===================== #

EMOJI5 = "❤️"

@Client.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, message):
    await message.react(emoji=EMOJI5, big=True)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.UPI_QR_CODE,
        caption=TXT.DONATE,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.DONATE_BTN
    )


# ===================== [ Privacy Command ] ===================== #


@Client.on_message(filters.private & filters.command(["privacy"]))
async def privacy(bot, message):
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    # await message.reply_photo(
    await message.reply_text(
        # photo=DS.START_IMG,
        text=TXT.PRIVACY,
        # parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.PRIVACY_BTN
    )


# ===================== [ Public Bot List cmd ] ===================== #


@Client.on_message(filters.private & filters.command(["bot_list"]))
async def bots(bot, message):
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    # await message.reply_photo(
    await message.reply_text(
        # photo=DS.START_IMG,
        text=TXT.BOTLIST,
        # parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.BOTLIST_BTN
    )


# ===================== [ Users Command ] ===================== #


@Client.on_message(filters.private & filters.user(DS.ADMIN)  & filters.command(["users"]))
async def all_db_users_here(client, message):
    start_t = time.time()
    ds = await message.reply_text("Processing...")
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
    total_users = await total_user()
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ds.edit(text=f"**--Bot Processed--** \n\n**Bot Started UpTime:** {uptime} \n**Bot Current Ping:** `{time_taken_s:.3f} ᴍꜱ` \n**All Bot Users:** `{total_users}`")


# ===================== [ Broadcast Command ] ===================== #


@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        ds = await message.reply_text("Wait... i am checking all bot users.")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await ds.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ started...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await ds.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
        await ds.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
        

# ===================== [ Restart Command ] ===================== #


@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    ds_msg = await b.send_message(text="**🔄 ALL PROCESS STOPPED !. BOT IS RESTARTING...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await ds_msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)


# ===================== [🔺 End Of Commands.py 🔺] ===================== #
