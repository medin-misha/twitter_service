from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Result, update, select, delete
from sqlalchemy.orm import selectinload, joinedload
from typing import List
from core import Image, Tweet, User, UserLikeTweet
from handlers import create, remove
from .shemas import User, UserLike, ReturnTweet


async def image_to_tweet(
    session: AsyncSession, tweet_id: int, images_ids: List[int]
) -> None:
    print(images_ids)
    stmt = (
        update(Image.__table__)
        .where(Image.id.in_(images_ids))
        .values(tweet_id=tweet_id)
    )
    await session.execute(stmt)
    await session.commit()


async def get_tweets(session: AsyncSession) -> List[ReturnTweet]:
    stmt = select(Tweet).options(selectinload("*")).order_by(Tweet.content)
    select_result: Result = await session.execute(stmt)
    tweets = []
    for tweet in select_result.scalars().all():
        tweet_data = ReturnTweet(
            id=tweet.id,
            content=tweet.content,
            author=User(
                id=tweet.autor.id,
                name=tweet.autor.name,
            ),
            attachments=[image.filename for image in tweet.attachments],
            likes=[UserLike(user_id=like.id, name=like.name) for like in tweet.likes],
        )
        tweets.append(tweet_data)

    return tweets


async def like_tweet(session: AsyncSession, tweet_id: int, user_id: int) -> bool:
    search_like_stmt = (
        select(UserLikeTweet.id)
        .where(UserLikeTweet.user_id == user_id)
        .where(
            UserLikeTweet.tweet_id == tweet_id,
        )
    )
    like_result: Result = await session.execute(search_like_stmt)
    like_id = like_result.scalars().all()
    if len(like_id) != 0:
        await remove(session=session, model=UserLikeTweet, id=like_id[0])
        return False
    await create(
        session=session,
        model=UserLikeTweet,
        data={"user_id": user_id, "tweet_id": tweet_id},
    )
    return True
