## BAN UNBAN (USER, CHANNEL), FORWARD MEDIA, NEW JOIN ##

from pyrogram import Client, filters
from pyrogram.types import Message, Chat
from pymongo import MongoClient

# MongoDB Setup
mongo_client = MongoClient("mongodb+srv://<username>:<password>@<cluster_url>")
db = mongo_client["your_database"]
banned_users = db["banned_users"]
banned_channels = db["banned_channels"]

LOG_CHANNEL = -1001234567890  # replace with your log channel ID
OWNER_ID = 123456789  # replace with your Telegram ID

# Helper Functions
async def is_user_banned(user_id: int) -> bool:
    return await banned_users.find_one({"user_id": user_id}) is not None

async def is_channel_banned(channel_id: int) -> bool:
    return await banned_channels.find_one({"channel_id": channel_id}) is not None

async def ban_user(user_id: int):
    await banned_users.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

async def unban_user(user_id: int):
    await banned_users.delete_one({"user_id": user_id})

async def ban_channel(channel_id: int):
    await banned_channels.update_one({"channel_id": channel_id}, {"$set": {"channel_id": channel_id}}, upsert=True)

async def unban_channel(channel_id: int):
    await banned_channels.delete_one({"channel_id": channel_id})

# Log New Users
@Client.on_message(filters.private & ~filters.service)
async def log_new_user(client, message: Message):
    if not await banned_users.find_one({"user_id": message.from_user.id}):
        await client.send_message(LOG_CHANNEL, f"#NewUser\nUsername: @{message.from_user.username}\nUser ID: <code>{message.from_user.id}</code>")

# Log New Channels
@Client.on_message(filters.channel & ~filters.service)
async def log_new_channel(client, message: Message):
    chat: Chat = message.chat
    if not await banned_channels.find_one({"channel_id": chat.id}):
        try:
            invite_link = await client.create_chat_invite_link(chat.id)
        except:
            invite_link = "Invite link not available"
        members = await client.get_chat_members_count(chat.id)
        await client.send_message(LOG_CHANNEL, f"#NewChannel\nTitle: <b>{chat.title}</b>\nID: <code>{chat.id}</code>\nMembers: {members}\nInvite: {invite_link}")

    # Forward media to log channel
    if message.media:
        await message.forward(LOG_CHANNEL)

    # Block processing if channel is banned
    if await is_channel_banned(chat.id):
        await message.reply("This channel is banned from using the bot. Contact the owner to unban.")
        return
    # Add your processing logic here

# Ban/Unban Commands
@Client.on_message(filters.private & filters.user(OWNER_ID) & filters.command("banuser"))
async def handle_ban_user(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        await ban_user(user_id)
        await message.reply("User banned.")
    except:
        await message.reply("Usage: /banuser <user_id>")

@Client.on_message(filters.private & filters.user(OWNER_ID) & filters.command("unbanuser"))
async def handle_unban_user(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        await unban_user(user_id)
        await message.reply("User unbanned.")
    except:
        await message.reply("Usage: /unbanuser <user_id>")

@Client.on_message(filters.private & filters.user(OWNER_ID) & filters.command("banchannel"))
async def handle_ban_channel(client, message: Message):
    try:
        channel_id = int(message.text.split()[1])
        await ban_channel(channel_id)
        await message.reply("Channel banned.")
    except:
        await message.reply("Usage: /banchannel <channel_id>")

@Client.on_message(filters.private & filters.user(OWNER_ID) & filters.command("unbanchannel"))
async def handle_unban_channel(client, message: Message):
    try:
        channel_id = int(message.text.split()[1])
        await unban_channel(channel_id)
        await message.reply("Channel unbanned.")
    except:
        await message.reply("Usage: /unbanchannel <channel_id>")
