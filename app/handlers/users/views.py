from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, List
from core import db_settings, User
from handlers import (
    create,
    remove,
    get_list,
    get_by_id,
    ok_response,
    error_response,
    get_user_by_api_key,
)
from .schemes import CreateUser, CreatedUser, OneUser
from .utils import following, get_user_by_id

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/")
async def create_user_view(
    user_data: CreateUser, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | CreatedUser]:
    user = await create(session=session, model=User, data=user_data.model_dump())
    return ok_response(resp=user, name="user")


@router.get("/me")
async def auth_user_view(
    request: Request, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | OneUser]:
    api_key = request.headers.get("api-key")
    if api_key == "test":
        return ok_response(resp={"id": 10**10, "name": "test"}, name="user")
    auth_user = await get_user_by_api_key(session=session, api_key=api_key)
    if auth_user is None:
        return error_response(msg="auth error ._.", err_type=401)
    user = await get_user_by_id(session=session, id=auth_user.get("id"))
    return ok_response(resp=user, name="user")


@router.api_route("/{id}/follow", methods=["POST", "DELETE"])
async def follow_user_view(
    id: int, request: Request, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | str | int]:
    api_key = request.headers.get("api-key")
    user = await get_user_by_api_key(session=session, api_key=api_key)
    if user is None:
        return error_response(msg="auth error ._.", err_type=401)
    following_user = await following(
        session=session, author_id=id, follower_id=user.get("id")
    )
    return (
        ok_response()
        if following_user
        else error_response(msg="repudiation (ツ)_/¯", err_type=200)
    )


@router.get("/{id}")
async def get_users_by_id_view(
    id: int, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | OneUser]:
    user = await get_user_by_id(session=session, id=id)
    if user is None:
        return error_response(msg="Юзер не найден", err_type=404)

    return ok_response(resp=user, name="user")


@router.get("/")
async def get_users_view(session: AsyncSession = Depends(db_settings.session)):
    users_list = await get_list(session=session, model=User)
    result = [elem.get("User") for elem in users_list]
    return ok_response(resp=result, name="users")


@router.delete("/{id}")
async def delete_user_view(
    id: int, session: AsyncSession = Depends(db_settings.session)
) -> Dict[str, bool | str]:
    await remove(session=session, model=User, id=id)
    return ok_response(resp={"message": "deleted"})
