from dotenv import load_dotenv
from functools import lru_cache

load_dotenv(".env")


class Settings:
    APP_NAME: str = ""
    PORT: str = "8000"
    CLOUDINARY_CLOUD_NAME: str = ""
    CLOUDINARY_API_SECRET: str = ""
    CLOUDINARY_API_KEY: str = ""
    CLOUDINARY_APP_NAME: str = ""
    JWT_SECRET: str = ""
    JWT_ALGORITHM: str = ""
    MySQL_DATABASE_URL: str = ""
    DB_HOST: str = ""
    DB_USERNAME: str = ""
    DB_PASSWORD: str = ""
    DB_NAME: str = ""
    FRONTEND_URL: str = ""

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()