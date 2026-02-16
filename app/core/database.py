from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    client: AsyncIOMotorClient = None
    db = None  # This will hold the specific database (e.g., local_dev_db)

db = Database()