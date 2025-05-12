# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

from config import DS
import asyncio, time, sys, os
from .Force_Sub import checkSub
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram import Client, filters, errors, enums
from .database import *
from .buttons import BTN
from .utils import log_channel_info
from translation import TXT

# ===================== [ Start Command ] ===================== #

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    await message.react(emoji="😘", big=True)
    user_id = int(message.from_user.id)
    chkuser = await is_user_exist(user_id)
    if not chkuser:
        await bot.send_message(
            DS.LOG_CHANNEL,
            f"#NewUser\n\nUsername: @{message.from_user.username}\nUser ID: <code>{message.from_user.id}</code>"
        )
        await insert(user_id)
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.START_PIC,
        caption=TXT.START,  #f"<b>Hello, {message.from_user.mention} 👋🏻\n\nI'm an auto-caption bot. I automatically edit captions for videos, audio files, and documents posted on channels.\n\nuse <code>/set_caption</code> to set caption\nUse<code>/delcaption</code> To delete caption and set caption to default.\n\nNote:All commands works on channels only</b>",
        reply_markup=BTN.START_BTN 
    )

# ===================== [ Help Command ] ===================== #

@Client.on_message(filters.command(["help"]) & filters.private)
async def help_cmd(bot, message):
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.START_PIC,
        caption=TXT.HELP,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.HELP_BTN
    )

# ===================== [ About Command ] ===================== #

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, message):
    is_joined = await checkSub(bot, message)
    if not is_joined: return
    await message.reply_photo(
        photo=DS.START_PIC,
        caption=TXT.ABOUT,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=BTN.ABOUT_BTN
      #  disable_web_page_preview=True 
    )


# ===================== [ Donate Command ] ===================== #

@Client.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, message):
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


# ===================== [ Stats Command ] ===================== #
 
# /stats command
@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["stats"]))
async def stats_command(client, message: Message):
    stats = await get_edit_stats()

    week_count = stats['week_stats'][0]['total_edits'] if stats['week_stats'] else 0
    month_count = stats['month_stats'][0]['total_edits'] if stats['month_stats'] else 0
    year_count = stats['year_stats'][0]['total_edits'] if stats['year_stats'] else 0
    total_count = stats['total_edits'][0]['total_edits'] if stats['total_edits'] else 0

    top_channels = stats['top_channels']
    top_channels_text = "No data"
    if top_channels:
        top_channels_text = ""
        for idx, channel in enumerate(top_channels, 1):
            try:
                chat = await client.get_chat(channel['channel_id'])
                name = chat.title or "Unknown"
                invite = chat.invite_link or "N/A"
            except Exception:
                name = "Unknown"
                invite = "N/A"

            top_channels_text += f"{idx}. {name} (`{channel['channel_id']}`) - {channel['edit_count']} edits\n"

    message_text = (
        f"**Total Edited Files:**\n"
        f"• This Week: {week_count}\n"
        f"• This Month: {month_count}\n"
        f"• This Year: {year_count}\n"
        f"• Total: {total_count}\n\n"
        f"**Top 3 Channels where I'm Most Used:**\n{top_channels_text}"
    )
    await message.reply(message_text)
    
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

# ===================== [ User Ban Command ] ===================== #
"""
@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["ban"]))
async def ban_user(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        await client.send_message(user_id, "You Are Banned To Use Me!\n\nContact My Owner To Get Unban\n👀 Owner: @THE_DS_OFFICIAL")
        await ban_user(user_id)
        await message.reply("User banned.")
    except:
        await message.reply("Usage: /ban <user_id>")

# ===================== [ User Unban Command ] ===================== #

@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["unban"]))
async def unban_user(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        await client.send_message(user_id, "You are Unbanned, Now you can use me 😃")
        await unban_user(user_id)
        await message.reply("User unbanned.")
    except:
        await message.reply("Usage: /unban <user_id>")
"""
# ===================== [ Channel Ban Command ] ===================== #

@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["banchannel"]))
async def banchannel(client, message: Message):
    try:
        channel_id = int(message.text.split()[1])
        await client.send_message(channel_id, "This Channel is Banned To Use Me!\n\nContact My Owner To Get Unban\n👀 Owner: @THE_DS_OFFICIAL")
        await log_channel_info(client, channel_id, "#Channel_Banned")
        await ban_channel(channel_id)
        await message.reply("Channel banned successfully.")
    except Exception as e:
        await message.reply("Usage: /banchannel <channel_id> \n\nError: {e}")

# ===================== [ Channel Unban Command ] ===================== #

@Client.on_message(filters.private & filters.user(DS.ADMIN) & filters.command(["unbanchannel"]))
async def unbanchannel(client, message: Message):
    try:
        channel_id = int(message.text.split()[1])
        await client.send_message(channel_id, "Channel is Unbanned, Now you can use me 😃")
        await log_channel_info(client, channel_id, "#Channel_Unbanned")
        await unban_channel(channel_id)
        await message.reply("Channel unbanned successfully.")
    except Exception as e:
        await message.reply("Usage: /unbanchannel <channel_id> \n\nError: {e}")
        
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
