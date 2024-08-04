# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #


from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import DS as Config
from .buttons import temp

# ===================== [ Force Sub Def ] ===================== #


async def checkSub(bot, message):
    userid = message.from_user.id
    try:
        user =await bot.get_chat_member(Config.FORCE_SUB, userid)
        if user.status == enums.ChatMemberStatus.BANNED:
            await message.reply_text("**Sorry, You're Banned. Contact my [Developer](https://t.me/THE_DS_OFFICIAL) to get unbanned.**")
            return False
        return True
    except UserNotParticipant:
        invite_link = await bot.export_chat_invite_link(Config.FORCE_SUB)
        join_button = InlineKeyboardMarkup([[
            InlineKeyboardButton('🤖 Join Channel 🤖', url=invite_link),
            InlineKeyboardButton('🔃 Refresh 🔃', url=f'https://t.me/{temp.U_NAME}?start=True')
            ]])
        await message.reply_text("**Please Join My Updates Channel to use this Bot!**\n\n**Due to Overload, Only Channel Subscribers can use this Bot!**", reply_markup=join_button)
        return False
    except Exception as e:
        print(e)
        await message.reply_text("Something went wrong. Contact my [Developer](https://t.me/THE_DS_OFFICIAL).")
        return False
    

# ===================== [🔺 End Of Force Sub 🔺] ===================== #
