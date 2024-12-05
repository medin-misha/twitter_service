"""
файл для модели tweet
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from .base import Base


class Tweet(Base):
    __tablename__ = "tweets"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    autor: Mapped["User"] = relationship(
        back_populates="tweets", uselist=False, lazy="select"
    )
    attachments: Mapped[List["Image"]] = relationship(uselist=True, lazy="joined")
    likes: Mapped[list["User"]] = relationship(
        back_populates="likes", uselist=True, secondary="usersliketweets"
    )
