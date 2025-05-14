# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os
from translation import TXT
from pyrogram import enums, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from config import DS

# ===================== [ BUTTON CODES ] ===================== #

class temp(object):
    U_NAME = None


class BTN(object):

    START_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕", url=f"https://t.me/Public_Caption_Bot?startchannel&admin=post_messages+edit_messages+delete_messages+invite_users+restrict_members+pin_messages+manage_chat+promote_members+manage_video_chats+anonymous")
        ],[
            InlineKeyboardButton("Dᴏɴᴀᴛᴇ 🤞🏻", callback_data="donate"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🕵🏻", callback_data="about")
        ],[
            InlineKeyboardButton("Mᴀʀᴋᴅᴏᴡɴꜱ ✨", callback_data="markdowns"),
            InlineKeyboardButton("Help ❗", callback_data="help"),
        ],[
            InlineKeyboardButton("𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ❓", callback_data="howtousecmd")
        ]]
    )


    HELP_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ABOUT MARKDOWN", callback_data = "markdowns")
        ],[
            InlineKeyboardButton("🏠 HOME", callback_data = "start"),
            InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
        ]]
    ) 

    ABOUT_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("HOW TO USE ME❓", callback_data="help")
        ],[
            InlineKeyboardButton("🏠 HOME", callback_data = "start"), 
            InlineKeyboardButton("CLOSE 🔒", callback_data = "close")
        ]]
    ) 
    
    MARKDOWN_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🏠 HOME", callback_data = "start"), 
            InlineKeyboardButton("CLOSE 🔐", callback_data = "close")
        ]]
    ) 
    
    DONATE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("Donate Via UPI ID", url=f"https://t.me/THE_DS_OFFICIAL")
        ],[
            InlineKeyboardButton("🏠 HOME", callback_data = "start"), 
            InlineKeyboardButton("CLOSE 🔐", callback_data = "close")
        ]]
    ) 
    
    PRIVACY_BTN = InlineKeyboardMarkup(
        [[ 
            InlineKeyboardButton("CLOSE 🔐", callback_data = "close")
        ]]
    )

    HTU_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ꜱʜᴏᴡᴄᴀᴘ", callback_data = "showcap")
        ],[
            InlineKeyboardButton("ꜱᴇᴛᴄᴀᴘ", callback_data = "setcap"),
            InlineKeyboardButton("ᴅᴇʟᴄᴀᴘ", callback_data = "delcap")
        ],[
            InlineKeyboardButton("ꜱᴇᴛʙᴜᴛᴛᴏɴ", callback_data = "button"),
            InlineKeyboardButton("ᴅᴇʟʙᴜᴛᴛᴏɴ", callback_data = "delbutton")
        ],[
            InlineKeyboardButton("ᴠᴀʀɪᴀʙʟᴇꜱ", callback_data = "variables")
        ],[
            InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data = "howtousecmd"),
            InlineKeyboardButton("Cʟᴏꜱᴇ 🔐", callback_data = "close")
        ]]
    )
    
    BACK_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data = "howtousecmd"),
            InlineKeyboardButton("Cʟᴏꜱᴇ 🔐", callback_data = "close")
        ]]
    ) 


# ===================== [ CALLBACK CODES ] ===================== #


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "start":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.START_PIC)
        )
        await query.message.edit_text(
            text=TXT.START,
            reply_markup=BTN.START_BTN,
            parse_mode=enums.ParseMode.HTML
        )            
    elif query.data == "donate":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.UPI_QR_PIC)
        )
        await query.message.edit_text(
            text=TXT.DONATE,
            reply_markup=BTN.DONATE_BTN,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "markdowns":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.MARKDOWN_PIC)
        )
        await query.message.edit_text(
            text=TXT.MARKDOWN,
            reply_markup=BTN.MARKDOWN_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.START_PIC)
        )
        await query.message.edit_text(
            text=TXT.ABOUT,
            reply_markup=BTN.ABOUT_BTN,
            parse_mode=enums.ParseMode.HTML
        )  
    elif query.data == "help":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.START_PIC)
        )
        await query.message.edit_text(
            text=TXT.HELP,
            reply_markup=BTN.HELP_BTN,
            parse_mode=enums.ParseMode.HTML
        )           
    elif query.data == "howtousecmd":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.START_PIC)
        )
        await query.message.edit_text(
            text=TXT.HTU_TXT,
            reply_markup=BTN.HTU_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "setcap":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.SETCAP_PIC)
        )
        await query.message.edit_text(
            text=TXT.SETCAP,
            reply_markup=BTN.BACK_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "delcap":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.DELCAP_PIC)
        )
        await query.message.edit_text(
            text=TXT.DELCAP,
            reply_markup=BTN.BACK_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "showcap":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.SHOWCAP_PIC)
        )
        await query.message.edit_text(
            text=TXT.SHOWCAP,
            reply_markup=BTN.BACK_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "button":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.SETBUTTON_PIC)
        )
        await query.message.edit_text(
            text=TXT.SETBUTTON,
            reply_markup=BTN.BACK_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "delbutton":
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(media=DS.DELBUTTON_PIC)
        )
        await query.message.edit_text(
            text=TXT.DELBUTTON,
            reply_markup=BTN.BACK_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "variables":
        await client.send_message(
            chat_id=query.message.chat.id,
            text=TXT.VAR,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=PRIVACY_BTN,
            disable_web_page_preview=True
        )
    else:
        await query.message.delete()

# ===================== [🔺 END OF BUTTON CODES 🔺] ===================== #
