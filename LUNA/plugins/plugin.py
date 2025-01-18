
from telehook import Filters

from LUNA import TeleHook, OWNER_ID
from LUNA.db import db


@TeleHook.on_message(Filters.command('plugin'))
async def plugin_cmd(client, message):
    user_id = message.from_user.id
    if user_id not in OWNER_ID:


    data = await db.check_user(user_id)
    if not data:
        await db.add_user(user_id, name)
        
    await message.reply_text(f'Hello {name}')