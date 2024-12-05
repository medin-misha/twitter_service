from pydantic import BaseModel, PositiveInt
from typing import List


class User(BaseModel):
    id: PositiveInt
    name: str


class UserLike(BaseModel):
    user_id: PositiveInt
    name: str


class BaseTweet(BaseModel):
    tweet_data: str
    tweet_media_ids: List[int] | None


class CreateTweet(BaseTweet):
    pass


class ReturnTweet(BaseModel):
    id: PositiveInt
    content: str
    attachments: List[str] | None
    author: User
    likes: List[UserLike] | None
