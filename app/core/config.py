from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_url: str = os.environ.get("db_url") if os.environ.get("db_url") is not None else "postgresql+asyncpg://postgres_user:postgres_password@192.168.5.194:5432/postgres_db"
    image_saver_url: str = os.environ.get("image_saver_url") if os.environ.get("image_saver_url") is not None else "http://192.168.5.194:9000/"


config = Settings()
