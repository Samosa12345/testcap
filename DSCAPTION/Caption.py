# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import os
from config import DS
import asyncio, re
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from .database import addCap, updateCap, chnl_ids
    

# ===================== [ Set Caption Command ] ===================== #


@Client.on_message(filters.command(["setcap", "setcaption"]) & filters.channel)
async def setCaption(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Example: /setcap set your caption ( Use <code>{file_name}</code> or <code>{post_caption}</code> to show file name\nAlso Use <code>{file_size}</code> to show file size</b>\n\n<b>For More Information Give /help Command To Bot</b>)"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Successfully Saved Your Caption.\n\nYour New Caption: `{caption}`")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Successfully Saved Your Caption.\n\nYour New Caption: `{caption}`")


# ===================== [ Delete Caption Command ] ===================== #


@Client.on_message(filters.command(["delcap", "delcaption", "delete_caption"]) & filters.channel)
async def delCaption(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b>Successfully deleted your caption..From now i will use my default caption</b>")
    except Exception as e:
        ds = await msg.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await ds.delete()
        return


# ===================== [ Edit Caption In Channel ] ===================== #


@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(file_name=file_name, file_size=get_size(file_size), post_caption = message.caption or message.text or "")
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = DS.DEF_CAP.format(file_name=file_name)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return

# ===================== [ Size Conversion Function ] ===================== #


def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])


# ===================== [🔺 End Of Caption.py 🔺] ===================== #
