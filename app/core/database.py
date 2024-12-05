from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .config import config


class DBSettings:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(echo=echo, url=db_url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,  # привязка движка к фабрики сессий
            expire_on_commit=False,  # кеширование обьектов в сессии
            autoflush=False,  # отключение произвольных действий со стороны ORM
            autocommit=False,  # отключение автоматических коммитов
        )

    async def session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_settings = DBSettings(db_url=config.db_url)
