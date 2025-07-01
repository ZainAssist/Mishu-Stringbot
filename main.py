#This string bot is made by Zainu #
#Please don't remove any credit 😔#
#Kindly join @About_Zain #
#https://github.com/RishuBot/Mishu-String#





import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from pyrogram.enums import ChatAction
from pyrogram.errors import UserNotParticipant
import requests
import time
from bs4 import BeautifulSoup
from flask import Flask
from threading import Thread
from pyrogram.errors import FloodWait
import pymongo
import re
from typing import Optional
import random

# Bot details from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Environment variable se token le raha hai #Your bot token 
CHANNEL_USERNAME = "About_Zain"  # Channel username
GROUP_USERNAME = "MusicOnMasti"  # Group username
API_HASH = "42a60d9c657b106370c79bb0a8ac560c"
API_ID = "14050586"

ADMIN_ID = int(os.getenv("ADMIN_ID", "7860277015"))  # Admin ID for new user notifications

# Flask app for monitoring
flask_app = Flask(__name__)
start_time = time.time()

# MongoDB setup
mongo_client = pymongo.MongoClient(
    os.getenv(
        "MONGO_URL","Mango db url dalooo"
    )
)
db = mongo_client[os.getenv("MONGO_DB_NAME", "Mishu-free-db")]
users_collection = db[os.getenv("MONGO_COLLECTION_NAME", "users")]

# Pyrogram bot client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@flask_app.route('/')
def home():
    uptime_minutes = (time.time() - start_time) / 60
    user_count = users_collection.count_documents({})
    return f"Bot uptime: {uptime_minutes:.2f} minutes\nUnique users: {user_count}"


@app.on_message(filters.command("start"))
async def start_message(client, message):
    user_id = message.from_user.id
    user = message.from_user
    # Simulate progress
    baby = await message.reply_text("[□□□□□□□□□□] 0%")

    # Simulate progress bar updates
    progress = [
        "[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"
    ]
    for i, step in enumerate(progress):
        await baby.edit_text(f"**{step}**")
        await asyncio.sleep(0.3)  # Adjust delay for progress updates

    # After progress bar reaches 100%, send welcome message
    await baby.edit_text("**❖ 💘Mishu-Zainu💘...**")
    await asyncio.sleep(1)
    await baby.delete()

    # Check if the user is a member of both channels
    if not (await is_user_in_channel(client, user_id, CHANNEL_USERNAME) and
            await is_user_in_group(client, user_id, GROUP_USERNAME)):
        await send_join_prompt(client, message.chat.id)
        return

    # Check if user is new
    if users_collection.count_documents({'user_id': user_id}) == 0:
        users_collection.insert_one({'user_id': user_id})
        # Notify admin about new user
        await client.send_message(
            chat_id=ADMIN_ID,
            text=(f"╔═══ ⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆ ══╗\n\n💡 **New User Alert**:\n\n"
                  f"👤 **User:** {message.from_user.mention}\n\n"
                  f"🆔 **User ID:** {user_id}\n\n"
                  f"📊 **Total Users:** {users_collection.count_documents({})}\n\n╚═════ ⋆★⋆ ═════╝")
        )

    # Random image selection
    image_urls = [
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg"
    ]
    random_image = random.choice(image_urls)

    # Inline buttons for channel join and help
    join_button_1 = InlineKeyboardButton("˹sυᴘᴘσꝛᴛ˼", url="https://t.me/+u7vfH3h-zNMzODZl")
    join_button_2 = InlineKeyboardButton("˹ᴅєᴠєʟσᴘєꝛ˼", url="https://t.me/Uff_Zainu")
    music_button = InlineKeyboardButton("˹ϻυsɪᴄ˼", url="https://t.me/MusicOnMasti")
    repo_button = InlineKeyboardButton("˹ ʀєᴘσ ˼", url="https://github.com/ZainAssist/Mishu-String")
    help_button = InlineKeyboardButton(" ˹ ɢєηєꝛᴧᴛє sᴛꝛɪηɢ ˼", callback_data="help_section")

    markup = InlineKeyboardMarkup([[help_button],[join_button_1,join_button_2],[music_button,repo_button]])

    # Send the welcome message with the random image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=random_image,
        caption=(f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•
┆◍ ʜᴇʏ {user.mention} 
└──────────────────────•
 ✦ ɪ'ᴍ ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ.
 ✦ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ.
 ✦ 𝛅ᴜᴘᴘᴏʀᴛ - ᴘʏʀᴏɢʀᴀᴍ | ᴛᴇʟᴇᴛʜᴏɴ.
 ✦ ηᴏ ɪᴅ ʟᴏɢ ᴏᴜᴛ ɪssᴜᴇ.

•──────────────────────•
 ❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ  :-  [˹ᴢᴀɪɴ](https://t.me/About_Zain) ❤️‍🔥
•──────────────────────•**"""),
        reply_markup=markup
    )


@app.on_callback_query(filters.regex("help_section"))
async def help_callback(client, callback_query: CallbackQuery):
    # Mini Web App buttons for session string generators
    mini_web_button_telethon = InlineKeyboardButton(
        "ᴛєʟєᴛʜση",
        web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#telethon,user")
    )
    mini_web_button_pyrogram = InlineKeyboardButton(
        "ᴘʏꝛσɢꝛᴧϻ",
        web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user")
    )
    mini_web_button_dez = InlineKeyboardButton(
        " ɢꝛᴧϻ ᴊs ",
        web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#gramjs,user")
    )
    mini_web_button_cute = InlineKeyboardButton(
        " ϻᴛ ᴄυᴛє ",
        web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#mtcute,user")
    )

    back_button = InlineKeyboardButton(" ˹ ʙᴧᴄᴋ ˼ ", callback_data="back_to_welcome")

    markup = InlineKeyboardMarkup([
        [mini_web_button_telethon,mini_web_button_pyrogram],
        [mini_web_button_dez,mini_web_button_cute],
        [back_button]
    ])

    help_message = "💡**ʜᴇʀᴇ ɪs ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴛᴏᴏʟs ᴍᴇᴛʜᴏᴅ.**\n\n**☞︎︎︎ ᴘʟᴇᴀsᴇ ᴄʜᴏᴏsᴇ ᴛʜᴇ ʟɪʙʀᴀʀʏ **\n\n**➻ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ**"
    await callback_query.message.edit_text(
        help_message,
        reply_markup=markup
    )


@app.on_callback_query(filters.regex("back_to_welcome"))
async def back_to_welcome(client, callback_query: CallbackQuery):
    user = callback_query.from_user

    image_urls = [
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg",
        "https://graph.org/file/d07dc208eaba21e922685-98f83a2138c89476d4.jpg"
    ]
    random_image = random.choice(image_urls)

    join_button_1 = InlineKeyboardButton("˹sυᴘᴘσꝛᴛ˼", url="https://t.me/+u7vfH3h-zNMzODZl")
    join_button_2 = InlineKeyboardButton("˹ᴅєᴠєʟσᴘєꝛ˼", url="https://t.me/Uff_Zainu")
    music_button = InlineKeyboardButton("˹ϻυsɪᴄ˼", url="https://t.me/MusicOnMasti")
    repo_button = InlineKeyboardButton("˹ʀєᴘσ˼", url="https://github.com/RishuBot/Mishu-Stringbot")
    help_button = InlineKeyboardButton("˹ ɢєηєꝛᴧᴛє sᴛꝛɪηɢ ˼", callback_data="help_section")

    markup = InlineKeyboardMarkup([[help_button],[join_button_1,join_button_2],[music_button,repo_button]])

    await callback_query.message.edit_text(
        text=(f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•
┆◍ ʜᴇʏ {user.mention} 
└──────────────────────•
 ✦ ɪ'ᴍ ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ.
 ✦ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ.
 ✦ 𝛅ᴜᴘᴘᴏʀᴛ - ᴘʏʀᴏɢʀᴀᴍ | ᴛᴇʟᴇᴛʜᴏɴ.
 ✦ ηᴏ ɪᴅ ʟᴏɢ ᴏᴜᴛ ɪssᴜᴇ 

•──────────────────────•
 ❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ  :-  [˹ᴢᴀɪɴ˼](https://t.me/About_Zain) ❤️‍🔥
•──────────────────────•**"""),
        reply_markup=markup
    )


async def is_user_in_channel(client, user_id, channel_username):
    """Check if the user is a member of the specified channel."""
    try:
        await client.get_chat_member(channel_username, user_id)
        return True
    except UserNotParticipant:
        return False
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False


async def send_join_prompt(client, chat_id):
    """Send a message asking the user to join both channels."""
    join_button_1 = InlineKeyboardButton("♡ Join ♡", url=f"https://t.me/{CHANNEL_USERNAME}")
    join_button_2 = InlineKeyboardButton("♡ Join ♡", url=f"https://t.me/{GROUP_USERNAME}")
    markup = InlineKeyboardMarkup([[join_button_1], [join_button_2]])
    await client.send_message(
        chat_id,
        "♡ You need to join both channels to use this bot.. ♡",
        reply_markup=markup,
    )


@app.on_message(filters.command("broadcast") & filters.user(7860277015))
async def broadcast_message(client, message):
    """Broadcast a message (text, photo, video, etc.) to all users."""
    if not (message.reply_to_message or len(message.command) > 1):
        await message.reply_text(
            "Please reply to a message or provide text to broadcast.\n\nUsage:\n"
            "/broadcast Your message here\nOR\nReply to any media with /broadcast"
        )
        return

    broadcast_content = message.reply_to_message if message.reply_to_message else message
    users = users_collection.find()
    sent_count = 0
    failed_count = 0

    await message.reply_text("Starting the broadcast...")

    for user in users:
        try:
            user_id = user["user_id"]

            if broadcast_content.photo:
                await client.send_photo(
                    chat_id=user_id,
                    photo=broadcast_content.photo.file_id,
                    caption=broadcast_content.caption or ""
                )
            elif broadcast_content.video:
                await client.send_video(
                    chat_id=user_id,
                    video=broadcast_content.video.file_id,
                    caption=broadcast_content.caption or ""
                )
            elif broadcast_content.document:
                await client.send_document(
                    chat_id=user_id,
                    document=broadcast_content.document.file_id,
                    caption=broadcast_content.caption or ""
                )
            elif broadcast_content.text:
                await client.send_message(
                    chat_id=user_id,
                    text=broadcast_content.text
                )
            sent_count += 1
        except FloodWait as e:
            print(f"FloodWait encountered for {e.value} seconds.")
            time.sleep(e.value)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")
            failed_count += 1

    await message.reply_text(
        f"Broadcast completed!\n\nMessages sent: {sent_count}\nFailed deliveries: {failed_count}"
    )


if __name__ == "__main__":
    Thread(target=lambda: flask_app.run(host="0.0.0.0", port=8080)).start()
    app.run()
