
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from LUNA import DATABASE_URI, LOGGER
from .users import UserOperations



class DATABASE(
    UserOperations
):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.udb = self.client["luna"]["users"]
        self.gdb = self.client["luna"]["group"]

        LOGGER.info("Database Connected...")
        self.initialize()

    def initialize(self):
        return


db = DATABASE(DATABASE_URI)


