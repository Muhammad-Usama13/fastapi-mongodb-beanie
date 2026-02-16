from app.core.database import db
from app.schemas.user import UserCreate
from bson import ObjectId
from bson.errors import InvalidId
from app.schemas.user import UserCreate, UserUpdate

async def update_user(user_id: str, update_data: UserUpdate) -> dict | None:
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        return None

    # exclude_unset=True ensures we only update fields the user provided in the request
    # Otherwise, it would overwrite existing data with "None"
    update_dict = update_data.model_dump(exclude_unset=True)
    
    # If the user sent an empty request body, just return the existing user
    if not update_dict:
        return await get_user_by_id(user_id)

    # Tell MongoDB to apply the specific updates
    await db.db["users"].update_one(
        {"_id": obj_id}, 
        {"$set": update_dict}
    )
    
    # Fetch and return the freshly updated user
    return await get_user_by_id(user_id)

async def delete_user(user_id: str) -> bool:
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        return False

    # Tell MongoDB to delete the document
    result = await db.db["users"].delete_one({"_id": obj_id})
    
    # Return True if a document was actually deleted, False if it wasn't found
    return result.deleted_count > 0
async def create_user(user_data: UserCreate) -> dict:
    # Convert Pydantic model to a dictionary
    user_dict = user_data.model_dump()
    
    # Insert into the 'users' collection
    result = await db.db["users"].insert_one(user_dict)
    
    # Add the MongoDB generated _id as a string 'id' for the response
    user_dict["id"] = str(result.inserted_id)
    return user_dict

async def get_user_by_id(user_id: str) -> dict | None:
    try:
        # Convert string ID to MongoDB ObjectId
        obj_id = ObjectId(user_id)
    except InvalidId:
        return None  # Return None if the ID format is totally invalid

    # Find the user
    user = await db.db["users"].find_one({"_id": obj_id})
    
    if user:
        user["id"] = str(user["_id"])
        return user
        
    return None
async def get_all_users() -> list[dict]:
    users = []
    # An empty dictionary {} means "find everything"
    cursor = db.db["users"].find({}) 
    
    # We iterate over the cursor asynchronously
    async for document in cursor:
        document["id"] = str(document["_id"])
        users.append(document)
        
    return users