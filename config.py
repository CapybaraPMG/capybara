from dotenv import load_dotenv
from functools import lru_cache
import os

load_dotenv(".env")


class Settings:
    APP_NAME: str = os.getenv("APP_NAME")
    PORT: str = os.getenv("PORT", "8000")
    CLOUDINARY_CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME", "")
    CLOUDINARY_API_SECRET: str = os.getenv("CLOUDINARY_API_SECRET", "")
    CLOUDINARY_API_KEY: str = os.getenv("CLOUDINARY_API_KEY", "")
    CLOUDINARY_APP_NAME: str = os.getenv("CLOUDINARY_APP_NAME", "")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "")
    MySQL_DATABASE_URL: str = os.getenv("MySQL_DATABASE_URL", "")
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_USERNAME: str = os.getenv("DB_USERNAME", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
