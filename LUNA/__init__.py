
import os
from telehook import TeleClient, logger
from echocore import EchoClient
from LUNA.config import config


CONFIG = config()


# Configure the bot token and webhook URL
BOT_TOKEN = CONFIG.BOT_TOKEN
WEBHOOK_URL = CONFIG.WEBHOOK_URL

DATABASE_URI = CONFIG.DATABASE_URI
ECHOCORE_TOKEN = CONFIG.ECHOCORE_TOKEN


OWNER_ID = CONFIG.OWNER_ID


BOT_ID = CONFIG.BOT_ID


# Initialize TeleHook with the plugins folder
TeleHook = TeleClient(
    token=BOT_TOKEN,
    url=WEBHOOK_URL,
    plugins={"root": "LUNA.plugins"}
)

ECHO = EchoClient(ECHOCORE_TOKEN)

LOGGER = logger