from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://{os.getenv('postgres_user')}:{os.getenv('postgres_password')}@{os.getenv('postgres_host')}"

    image_saver_url: str = os.environ.get("image_service_host")


config = Settings()
print(config.image_saver_url)