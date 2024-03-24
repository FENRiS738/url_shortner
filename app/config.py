from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "mysql://localhost:3306"
    # db_url: str = "mongodb+srv://as420738:VVOfwmMLPOkzGmdd@cluster0.e1zoimv.mongodb.net/?retryWrites=true&w=majority"
    db_name: str = "url_shortner"

    class Config:
        env_file = '.env'

        
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings