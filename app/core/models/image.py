"""
файл для модели image    
"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class Image(Base):
    __tablename__ = "images"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(unique=True)
    tweet_id: Mapped[str] = mapped_column(
        ForeignKey("tweets.id", ondelete="CASCADE"),
        nullable=True,
    )


#     filename: Mapped[str] = mapped_column(unique=True, primary_key=True)
#     tweet_id: Mapped[int] = mapped_column(ForeignKey("tweet.id"), nullable=True)
