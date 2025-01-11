
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from LUNA import DATABASE_URI, LOGGER
from .users import UserOperations



class DATABASE(
    UserOperations
):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.centraldb = self.client["luna"]


        self.initialize()
        LOGGER.info("Database Connected...")

    def initialize(self):
        self.udb = self.centraldb["users"]
        self.gdb = self.centraldb["group"]
        return


db = DATABASE(DATABASE_URI)


