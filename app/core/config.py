from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://{os.getenv('postgres_user')}:{os.getenv('postgres_password')}@{os.getenv('postgres_host')}"

    image_saver_url: str = (
        os.environ.get("image_saver_url")
        if os.environ.get("image_saver_url") is not None
        else "http://192.168.5.194:9000/"
    )


config = Settings()
