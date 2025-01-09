

from GramDB import GramDB, GramDBAsync

from LUNA import GRAMDB_URI, LOGGER
from datetime import datetime



class DATABASE():
    """
    A class to manage the database operations using GramDB.

    Attributes:
        db (GramDB): An instance of the GramDB class initialized with the provided URI.
        table_schemas (dict): A dictionary defining table names and their corresponding schema.
    """
    def __init__(self, uri):
        """
        Initializes the Database instance and creates tables if they don't exist.

        Args:
            uri (str): The URI string to connect to the GramDB database.
        """
        self.async_manager = GramDBAsync()
        self.db = GramDB(uri, self.async_manager)
        self.initialize()

    def initialize(self):
        self.table_schemas = {
            "users": ("_id", "name", "coins", "joined_date", "is_scanned")
        }
        self.async_manager.run_async(self.create_table())
        # self.async_manager.run_async(self.create_cache())

    async def create_table(self):
        """
        Asynchronously creates a table if it doesn't exist.
        """
        for table_name, schema in self.table_schemas.items():
            if not await self.db.check_table(table_name):
                await self.db.create_one(table_name, schema)

    async def create_cache(self):
        """
        Creates Cache memory for Users and Groups
        """
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
        
    
    async def check_user(self, user_id: int):
        data = await self.db.find_one(
            "users",
            {
                "_id": user_id
            }
        )
        if data:
            return data
        else:
            return None

    async def add_user(
        self,
        user_id: int,
        name: str,
        coins: str,
        is_scanned: bool
    ):
        data = await self.check_user(user_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            try:
                await self.db.insert_one(
                    "users",
                    {
                        "_id": user_id,
                        "name": name,
                        "coins": coins,
                        "joined_date": str_date,
                        "is_scanned": is_scanned
                    }
                )
            except Exception as e:
                LOGGER.error(f"Error adding user to database: {e}")
            return
        
    def close(self):
        self.db.close()


db = DATABASE(GRAMDB_URI)


