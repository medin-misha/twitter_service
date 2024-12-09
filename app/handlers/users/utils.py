from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.orm import selectinload
from typing import Any, Callable, Type
from core import Image, User, Tweet, UserFallow
from handlers import create, remove
from .schemes import CreateUser, OneUser


async def following(session: AsyncSession, author_id: int, follower_id: int) -> bool:
    search_following_stmt = (
        select(UserFallow.id)
        .where(UserFallow.follower_id == follower_id)
        .where(
            UserFallow.autor_id == author_id,
        )
    )
    search_followr_result: Result = await session.execute(search_following_stmt)
    following_id = search_followr_result.scalars().all()
    if len(following_id) != 0:
        await remove(session=session, model=UserFallow, id=following_id[0])
        return False
    await create(
        session=session,
        model=UserFallow,
        data={"autor_id": author_id, "follower_id": follower_id},
    )
    return True


async def get_user_by_id(session: AsyncSession, id: int) -> OneUser | None:
    if not 0 < id < 10 * 5:
        return None
    result = await session.execute(
        select(User)
        .options(selectinload(User.followers))
        .options(selectinload(User.following))
        .options(selectinload(User.tweets))
        .where(User.id == id)
    )
    user = result.scalar()
    if user is None:
        return None

    return OneUser(
        id=user.id,
        name=user.name,
        followers=[
            {"id": follower.id, "name": follower.name} for follower in user.followers
        ],
        following=[
            {"id": following.id, "name": following.name} for following in user.following
        ],
    )
