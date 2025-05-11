# (c) @Bisal
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import motor.motor_asyncio
from config import DS

client = motor.motor_asyncio.AsyncIOMotorClient(DS.DB_URL)
db = client[DS.DB_NAME]
chnl_ids = db.chnl_ids
users = db.users
buttons_col = db["channel_buttons"]
chnl_ids = db["channel_captions"]

#insert user data
async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass
        
# Total User
async def total_user():
    user = await users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)
                     
async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})

# Save buttons to DB
async def set_channel_buttons(channel_id, buttons_list):
    # Manually convert to dicts
    serialized = [
        [{"text": btn.text, "url": btn.url} for btn in row]
        for row in buttons_list
    ]

    await buttons_col.update_one(
        {"channel_id": channel_id},
        {"$set": {"buttons": serialized}},
        upsert=True
    )

# Get buttons from DB
async def get_channel_buttons(channel_id):
    data = await buttons_col.find_one({"channel_id": channel_id})
    if not data:
        return []

    return [
        [InlineKeyboardButton(text=btn["text"], url=btn["url"]) for btn in row]
        for row in data["buttons"]
    ]
