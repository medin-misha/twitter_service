from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.dialects.postgresql import insert
from typing import Callable, List, Any
from core import Image, User, Tweet


async def create(
    session: AsyncSession,
    model: Image | User | Tweet,
    data: dict,
) -> dict[Any]:
    stmt = insert(model.__table__).values(**data).returning(model.__table__)
    stmt_result: Result = await session.execute(stmt)
    await session.commit()
    return dict(stmt_result.mappings().one())


async def get_by_id(
    session: AsyncSession, model: Image | User | Tweet, id: int
) -> dict | None:
    if 0 < id < 10**5:
        stmt = select(model).options(selectinload("*")).where(model.id == id)
        select_result: Result = await session.execute(stmt)
        return select_result.mappings().one_or_none()
    return None

async def get_list(session: AsyncSession, model: Image | User | Tweet) -> List[dict]:
    stmt = select(model).options(selectinload("*")).order_by(model.id)
    select_result: Result = await session.execute(stmt)
    return select_result.mappings().all()


async def remove(
    session: AsyncSession,
    model: Image | User | Tweet,
    id: int,
) -> None:
    stmt = delete(model.__table__).where(model.id == id)

    await session.execute(stmt)
    await session.commit()


async def get_user_by_api_key(session: AsyncSession, api_key: str) -> dict | None:
    stmt = select(User.__table__._columns.name, User.__table__._columns.id).where(
        User.key == api_key
    )
    select_result = await session.execute(stmt)
    return select_result.mappings().one_or_none()
