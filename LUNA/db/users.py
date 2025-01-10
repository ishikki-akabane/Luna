
from datetime import datetime
from LUNA import LOGGER


class UserOperations:
    """
    A class that handles user-related operations.
    """
    async def check_user(self, user_id: int):
        data = await self.udb.find_one(
            {"_id": user_id}
        )
        if data:
            return data
        else:
            return None

    async def add_user(
        self,
        user_id: int,
        name: str,
        username: str=None
    ):
        data = await self.check_user(user_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            try:
                await self.udb.insert_one(
                    {
                        "_id": user_id,
                        "name": name,
                        "username": username,
                        "date": str_date,
                    }
                )
            except Exception as e:
                LOGGER.error(f"Error adding user to database: {e}")
            return