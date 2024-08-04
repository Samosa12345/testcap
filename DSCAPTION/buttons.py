# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os
from translation import TXT
from pyrogram import enums, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import DS

# ===================== [ BUTTON CODES ] ===================== #

class temp(object):
    U_NAME = None


class BTN(object):

    START_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕", url=f"https://t.me/{temp.U_NAME}?startchannel=True") #botstart
        ],[
            InlineKeyboardButton("❗ Help ", callback_data="help"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🕵️", callback_data="about")
        ],[
            InlineKeyboardButton("✨ Mᴀʀᴋᴅᴏᴡɴꜱ ", callback_data="markdowns"),
            InlineKeyboardButton("Dᴏɴᴀᴛᴇ 🤞🏻", callback_data="donate")
        ],[
            InlineKeyboardButton("👨🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ 👨🏻‍💻", url=f"https://t.me/THE_DS_OFFICIAL")
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
            InlineKeyboardButton("HOW TO USE ME❓", callback_data = "help")
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

    BOTLIST_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🏠 HOME", callback_data = "start"), 
            InlineKeyboardButton("CLOSE 🔐", callback_data = "close")
        ]]
    ) 


# ===================== [ CALLBACK CODES ] ===================== #


@Client.on_callback_query()
async def cb_handler(bot, message):
    if query.data == "start":
        await Client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto=DS.START_PIC
        )
        await query.message.edit_text(
            text=TXT.START,
            reply_markup=BTN.START_BTN,
            parse_mode=enums.ParseMode.HTML
        )            
    elif query.data == "donate":
        await Client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto=DS.UPI_QR_CODE
        )
        await query.message.edit_text(
            text=TXT.DONATE,
            reply_markup=BTN.DONATE_BTN,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "markdowns":
        await Client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto=DS.START_PIC
        )
        await query.message.edit_text(
            text=TXT.MARKDOWN,
            reply_markup=BTN.MARKDOWN_BTN,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        await Client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto=DS.START_PIC
        )
        await query.message.edit_text(
            text=TXT.ABOUT,
            reply_markup=BTN.ABOUT_BTN,
            parse_mode=enums.ParseMode.HTML
        )  
    elif query.data == "help":
        await Client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto=DS.START_PIC
        )
        await query.message.edit_text(
            text=TXT.HELP,
            reply_markup=BTN.HELP_BTN,
            parse_mode=enums.ParseMode.HTML
        )           
    else:
        await message.message.delete()

# ===================== [🔺 END OF BUTTON CODES 🔺] ===================== #
