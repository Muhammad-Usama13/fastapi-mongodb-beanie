from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    MONGODB_URI: str
    OPENAI_API_KEY: str
    SECRET_KEY: str
    db_name: str = "local_dev_db"  # Default value if not provided in .env

    # This tells Pydantic to read from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# lru_cache ensures we only read the .env file once and reuse the Settings instance
@lru_cache()
def get_settings() -> Settings:
    return Settings()