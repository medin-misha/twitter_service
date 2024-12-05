from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict
import json
from handlers import (
    create,
    remove,
    get_list,
    ok_response,
    error_response,
    get_user_by_api_key,
    get_by_id,
)
from core import Tweet, db_settings, UserLikeTweet
from .shemas import CreateTweet, ReturnTweet
from .utils import image_to_tweet, get_tweets, like_tweet

router = APIRouter(prefix="/api/tweets", tags=["tweet"])


@router.post("")
async def create_tweet_view(
    tweet_data: CreateTweet,
    request: Request,
    session: AsyncSession = Depends(db_settings.session),
) -> Dict[str, bool | int] | Dict[str, str | int]:
    user_key: str = request.headers.get("api-key")
    user = await get_user_by_api_key(session=session, api_key=user_key)

    if user is None:
        return error_response(msg="auth error ._.", err_type=401)

    tweet = await create(
        session=session,
        model=Tweet,
        data={"content": tweet_data.tweet_data, "user_id": user.get("id")},
    )

    await image_to_tweet(
        session=session,
        images_ids=tweet_data.tweet_media_ids,
        tweet_id=tweet.get("id"),
    )
    return ok_response(resp=tweet.get("id"), name="tweet_id")


@router.get("")
async def get_tweet_view(
    request: Request, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | List[ReturnTweet]]:
    tweets = await get_tweets(session=session)
    return ok_response(resp=tweets, name="tweets")


@router.api_route("/{id}/likes", methods=["POST", "DELETE"])
async def like_tweet_view(
    id: int, request: Request, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | str | int]:
    user_key = request.headers.get("api-key")
    user = await get_user_by_api_key(session=session, api_key=user_key)
    if user is None:
        return error_response(msg="auth error ._.", err_type=401)
    liked_tweet = await like_tweet(session=session, tweet_id=id, user_id=user.get("id"))
    return (
        ok_response()
        if liked_tweet
        else error_response(msg="like delete (ツ)_/¯", err_type=200)
    )


@router.delete("/{id}")
async def delete_tweet_view(
    id: int, request: Request, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | str | int]:
    user_key = request.headers.get("api-key")
    user = await get_user_by_api_key(session=session, api_key=user_key)
    if user is None:
        return error_response(msg="auth error ._.", err_type=401)

    tweet = await get_by_id(session=session, model=Tweet, id=id)
    if user.get("id") == tweet.get("Tweet").user_id:
        await remove(session=session, model=Tweet, id=id)
        return ok_response(resp=None, name=None)
    return error_response(
        msg="don't infringe on other users' tweets (＃＞＜) ", err_type=401
    )
