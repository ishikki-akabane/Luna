
from telehook import Filters
from telehook.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from LUNA import TeleHook, OWNER_ID
from LUNA.db import db


@TeleHook.on_message(Filters.command('plugin'))
async def plugin_cmd(client, message: Message):
    user_id = message.from_user.id
    if user_id not in OWNER_ID:
        return await message.reply_text("**You are not authorised to use it!!**")
    
    await message.reply_text(
        """
ECHOSTORE

Welcome to EchoStore,
Get 100+ Plugins for building your perfect Telegram bot

- Easy to install
- 100% Bug free
- Verified by Developers
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="< S H O P >", url="https://t.me/ishikki")
                ]
            ]
        )
    )