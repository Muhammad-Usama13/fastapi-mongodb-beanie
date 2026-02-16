from fastapi import APIRouter, Depends
from app.core.config import Settings, get_settings

# Thin routing layer
router = APIRouter(prefix="/config", tags=["Configuration"])

@router.get("/verify")
async def verify_config(settings: Settings = Depends(get_settings)):
    """
    Returns a masked version of the configuration to prove Dependency Injection works.
    Never return real secrets in a production endpoint!
    """
    return {
        "message": "Dependencies injected successfully!",
        "mongodb_host": settings.MONGODB_URI.split("@")[-1] if "@" in settings.MONGODB_URI else settings.MONGODB_URI,
        "openai_key_prefix": settings.OPENAI_API_KEY[:5] + "..."
    }