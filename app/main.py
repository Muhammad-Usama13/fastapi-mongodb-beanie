from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import get_settings
from app.core.database import db
from app.routers import example, user

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    
    # 1. Connect to MongoDB client
    db.client = AsyncIOMotorClient(settings.MONGODB_URI)
    
    # 2. Select the specific database using the db_name from config
    db.db = db.client[settings.db_name] 
    
    print(f"Connected to MongoDB: {settings.db_name}")
    
    yield
    
    db.client.close()
    print("Closed MongoDB connection.")

app = FastAPI(lifespan=lifespan, title="Modular FastAPI App")

# Include the routers
app.include_router(example.router)
app.include_router(user.router)