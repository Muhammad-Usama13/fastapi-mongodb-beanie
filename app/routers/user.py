from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services import user as user_service
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserCreate):
    """Adds a new user to the database."""
    new_user = await user_service.create_user(user)
    return new_user

@router.get("/", response_model=list[UserResponse])
async def get_all_users():
    """Fetches a complete list of all users from the database."""
    users = await user_service.get_all_users()
    return users
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    """Fetches a user by their ID."""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    """Updates an existing user's details."""
    updated_user = await user_service.update_user(user_id, user_update)
    
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    """Deletes a user by their ID."""
    deleted = await user_service.delete_user(user_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return None