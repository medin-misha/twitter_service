"""
файл для модели user
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import List
from .base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    key: Mapped[str] = mapped_column(unique=True)
    tweets: Mapped[List["Tweet"]] = relationship(
        back_populates="autor", lazy="selectin", uselist=True
    )
    likes: Mapped[list["Tweet"]] = relationship(
        back_populates="likes", uselist=True, secondary="usersliketweets", lazy="selectin"
    )
    followers: Mapped[List["User"]] = relationship(
        back_populates="following",
        uselist=True,
        secondary="usersfallows",
        primaryjoin="User.id == UserFallow.autor_id",
        secondaryjoin="User.id == UserFallow.follower_id",
        lazy="selectin",
    )
    following: Mapped[List["User"]] = relationship(
        back_populates="followers",
        uselist=True,
        secondary="usersfallows",
        primaryjoin="User.id == UserFallow.follower_id",
        secondaryjoin="User.id == UserFallow.autor_id",
        lazy="selectin",
    )


#     name: Mapped[str] = mapped_column(String(100))
#     key: Mapped[str] = mapped_column(unique=True)
#
# primaryjoin="User.id == UserFallow.autor_id"
# primaryjoin="User.id == UserFallow.follower_if"

#     following_ids: Mapped[List[int]] = relationship(
#         back_populates="autor_id",
#         secondary="userfollow",
#         secondaryjoin="user.id == userfollow.autor_id",
#     )
#     followers_id: Mapped[List[int]] = relationship(
#         back_populates="autor_id",
#         secondary="userfollow",
#         secondaryjoin="user.id == userfollow.follower_id",
#     )
#
#     liked_tweets: Mapped[List["Tweet"]] = relationship(
#         back_populates="liked_users", uselist=True, secondary="userliketweet"
#     )
