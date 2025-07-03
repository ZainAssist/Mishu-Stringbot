from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🍹 Start Generating Session 🍹", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("💠 Join Our Chatting Group 💠", url="https://t.me/+u7vfH3h-zNMzODZl")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Join Our Music Group ♥", url="https://t.me/MusicOnMasti")],
    ]

    START = """
**Hey {}

Welcome to {}

If you don't trust this bot, 
> Please stop reading this message
> Delete this chat

Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !

By @About_Zain**
    """

    HELP = """
🌟 **Available Commands** 🌟

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @About_Zain

Source Code : [Click Here](https://github.com/ZainAssist/Mishu-Stringbot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @CoderELAlpha
    """
