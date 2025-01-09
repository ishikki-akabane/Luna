
import os
from telehook import TeleClient, logger
from LUNA.config import config


CONFIG = config()


# Configure the bot token and webhook URL
BOT_TOKEN = CONFIG.token
WEBHOOK_URL = "https://pup-solid-publicly.ngrok-free.app/"


# Initialize TeleHook with the plugins folder
TeleHook = TeleClient(
    token=BOT_TOKEN,
    url=WEBHOOK_URL,
    plugins={"root": "bot.plugins"}
)

LOGGER = logger