# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import motor.motor_asyncio
from config import DS

# ===================== [ MongoDB Client Creation ] ===================== #

client = motor.motor_asyncio.AsyncIOMotorClient(DS.DB_URL)
db = client[DS.DB_NAME]
chnl_ids = db.chnl_ids
users = db.users
banned_users = db.banned_users
banned_channels = db.banned_channels
buttons_col = db["channel_buttons"]
chnl_ids = db["channel_captions"]
edits_col = db['edits_col']

# ===================== [ Insert User & Channel id Functions ] ===================== #

async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass

async def insert_chnl(chnl_id):
    chnl = {"_id": chnl_id}
    try:
        await chnl_ids.insert_one(chnl)
    except:
        pass

# ===================== [ Check For Existance ] ===================== #

async def is_user_exist(user_id):
    user = await users.find_one({'_id': user_id})
    return bool(user)

async def is_chnl_exist(chnl_id):
    chnl = await chnl_ids.find_one({'_id': chnl_id})
    return bool(chnl)

# ===================== [ Get User Data ] ===================== #

async def total_user():
    user = await users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)

# ===================== [ Update & Add Caption ] ===================== #

async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})


# ===================== [ User & Channel Ban Data ] ===================== #

async def is_user_banned(user_id: int) -> bool:
    chk = await banned_users.find_one({"user_id": user_id})
    return bool(chk)
    
async def ban_user(user_id: int):
    await banned_users.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

async def unban_user(user_id: int):
    await banned_users.delete_one({"user_id": user_id})

async def is_channel_banned(channel_id: int) -> bool:
    data = await banned_channels.find_one({"channel_id": channel_id})
    return bool(data)
    
async def ban_channel(channel_id: int):
    await banned_channels.update_one({"channel_id": channel_id}, {"$set": {"channel_id": channel_id}}, upsert=True)

async def unban_channel(channel_id: int):
    await banned_channels.delete_one({"channel_id": channel_id})


# ===================== [ Inline Button Data of channel ] ===================== #

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

# ===================== [ Stats Command Data  ] ===================== #

# Record edit function
async def record_edit(channel_id, timestamp=None):
    if not timestamp:
        timestamp = datetime.utcnow()  # Always store UTC

    await edits_col.update_one(
        {'channel_id': channel_id},
        {'$inc': {'edit_count': 1}, '$push': {'timestamps': timestamp}},
        upsert=True
    )

async def get_edit_stats():
    now = datetime.utcnow()
    one_week_ago = now - timedelta(weeks=1)
    one_month_ago = now - timedelta(weeks=4)
    one_year_ago = now - timedelta(weeks=52)

    async def run_aggregate(pipeline):
        results = []
        async for doc in edits_col.aggregate(pipeline):
            results.append(doc)
        return results

    week_stats = await run_aggregate([
        {"$unwind": "$timestamps"},
        {"$match": {"timestamps": {"$gte": one_week_ago}}},
        {"$group": {"_id": None, "total_edits": {"$sum": 1}}}
    ])

    month_stats = await run_aggregate([
        {"$unwind": "$timestamps"},
        {"$match": {"timestamps": {"$gte": one_month_ago}}},
        {"$group": {"_id": None, "total_edits": {"$sum": 1}}}
    ])

    year_stats = await run_aggregate([
        {"$unwind": "$timestamps"},
        {"$match": {"timestamps": {"$gte": one_year_ago}}},
        {"$group": {"_id": None, "total_edits": {"$sum": 1}}}
    ])

    total_edits = await run_aggregate([
        {"$unwind": "$timestamps"},
        {"$group": {"_id": None, "total_edits": {"$sum": 1}}}
    ])

    top_channels = await run_aggregate([
        {"$project": {"channel_id": 1, "edit_count": {"$size": "$timestamps"}}},
        {"$sort": {"edit_count": -1}},
        {"$limit": 3}
    ])

    return {
        'week_stats': week_stats,
        'month_stats': month_stats,
        'year_stats': year_stats,
        'total_edits': total_edits,
        'top_channels': top_channels
    }


# ===================== [ THE END ] ===================== #
