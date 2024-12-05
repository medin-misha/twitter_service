from pydantic import BaseModel, PositiveInt
from annotated_types import Annotated, MaxLen, MinLen


class BaseUser(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(100)]
    key: Annotated[str, MinLen(10)]


class CreateUser(BaseUser):
    pass


class CreatedUser(BaseUser):
    id: PositiveInt


class OneUser(BaseModel):
    id: PositiveInt
    name: Annotated[str, MinLen(2), MaxLen(100)]
    following: list | None = None
    followers: list | None = None
    tweets: list | None = None
