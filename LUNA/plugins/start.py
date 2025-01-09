

from LUNA import TeleHook
from telehook import Filters
from LUNA.db import db

@TeleHook.on_message(Filters.command('start'))
async def start_cmd(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    data = await db.check_user(user_id)
    if data:
        pass
    else:
        await db.add_user(user_id, name, 100, False)
    message.reply_text(f'Hello {name}')