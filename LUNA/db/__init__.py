
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from LUNA import DATABASE_URI, LOGGER
from .users import UserOperations


class DATABASE(
    UserOperations
):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.udb = self.client["user_db"]["db"]
        self.adb = self.client["app_db"]["db"]
        self.initialize()

    def initialize(self):
        return

    async def create_cache(self):
        self.CACHE_USERS = []
        self.CACHE_GROUPS = []
        self.WELCOME_IDS = []
        
        all_user = await self.db.find("users", {})
        for user in all_user:
            self.CACHE_USERS.append(user["_id"])

        all_group = await self.db.find("groups", {})
        for group in all_group:
            self.CACHE_GROUPS.append(group["_id"])

        all_welcome_data = await self.db.find("welcome", {})
        for welcome_temp in all_welcome_data:
            self.WELCOME_IDS.append(welcome_temp["template_id"])


db = DATABASE(DATABASE_URI)

CACHE_USERS = db.CACHE_USERS
CACHE_GROUPS = db.CACHE_GROUPS
WELCOME_IDS = db.WELCOME_ID


