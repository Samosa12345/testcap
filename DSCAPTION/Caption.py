# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

import asyncio 
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import Message, InlineKeyboardMarkup
from .utils import *
from .database import *
from config import DS
from translation import TXT 

# ===================== [ Set Caption Command ] ===================== #

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


# ===================== [ Delete Caption Command ] ===================== #


@Client.on_message(filters.command(["delcap", "delcaption"]) & filters.channel)
async def delete_caption(_, message: Message):
    chnl_id = message.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        await message.reply("<b>Successfully deleted your custom caption. Default will now be used.</b>")
    except Exception as e:
        reply = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await reply.delete()


# ===================== [ See Caption Template Command ] ===================== #


@Client.on_message(filters.command(["preview", "showcap"]) & filters.channel)
async def preview_caption(_, message: Message):
    chnl_id = message.chat.id
    cap_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if cap_data and "caption" in cap_data:
        await message.reply(f"<b>Your saved caption template:</b>\n<code>{cap_data['caption']}</code>")
    else:
        await message.reply("<b>No custom caption set. Default will be used.</b>")


# ===================== [ Variable Command ] ===================== #


@Client.on_message(filters.command("variables") & filters.channel)
async def show_placeholders(_, message: Message):
    await message.reply(TXT.VAR)


# ===================== [ Setbutton Command ] ===================== #


@Client.on_message(filters.command(["button", "setbutton"]) & filters.channel)
async def set_buttons(bot, message):
    if not message.reply_to_message:
        return await message.reply("Please reply to a media message and provide button data like, \n\nEg. <code>/setbutton Watch Now = https://example.com | Trailer = https://youtube.com</code> \n\n⬆️ or ⬇️ \n\n<code>/setbutton More Info = https://site.com\nJoin = https://t.me/Bots_Office</code>")    

    raw = message.text.split(None, 1)
    if len(raw) < 2:
        return await message.reply("No button format found.")

    buttons = await parse_buttons(raw[1])
    if not buttons:
        return await message.reply("Invalid button format.")

    await set_channel_buttons(message.chat.id, buttons)
    await message.reply("Buttons saved for this channel!")


# ===================== [ Button Removal Command ] ===================== #


@Client.on_message(filters.command("delbutton") & filters.channel)
async def del_buttons(bot, message):
    await buttons_col.delete_one({"channel_id": message.chat.id})
    await message.reply("Buttons deleted for this channel.")


# ===================== [ Edit Caption In Channel & Other Function ] ===================== #


@Client.on_message(filters.channel)
async def handle_channel_message(bot, message: Message):
    chnl_id = message.chat.id
    file = message.document or message.video or message.audio
    if not file:
        return

    if await is_channel_banned(chnl_id):
        return

    if not await is_chnl_exist(chnl_id):
        try:
            invite_link = await bot.export_chat_invite_link(chnl_id)
        except ChatAdminRequired:
            invite_link = "Invite link not available"
        except Exception:
            invite_link = "Unknown"

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
        await insert_chnl(chnl_id)

    default_caption = message.caption or ""
    cap_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    template = cap_data["caption"] if cap_data else DS.DEF_CAP.format(caption=clean_filename(default_caption))

    new_caption = format_caption(
        template,
        filename=file.file_name,
        filesize=file.file_size,
        caption=default_caption,
        duration=getattr(file, "duration", None),
        height=getattr(file, "height", None),
        width=getattr(file, "width", None),
        mimetype=getattr(file, "mime_type", None),
        mediatype="Document" if message.document else "Video" if message.video else "Audio",
        title=getattr(file, "title", None),
        artist=getattr(file, "performer", None)
    )

    buttons = await get_channel_buttons(chnl_id)
    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None

    try:
        await message.edit_caption(new_caption, reply_markup=reply_markup)
        await record_edit(chnl_id) 
    except Exception as e:
        print(f"Edit failed: {e}")

# ===================== [ THE END ] ===================== #

        
