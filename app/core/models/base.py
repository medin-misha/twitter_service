from sqlalchemy.orm import (
    declarative_base,
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)


# class Base(DeclarativeBase):
#     __abstract__ = True
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#
#     @declared_attr.directive
#     def __tablename__(cls):
#         return f"{cls.__name__.lower()}"

Base = declarative_base()
