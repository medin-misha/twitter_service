from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, UploadFile, Request, Form
from annotated_types import Annotated
from typing import Dict
from handlers import (
    ok_response,
    error_response,
    create,
    get_by_id,
    remove,
    get_user_by_api_key,
    get_image
)
from core import Image, db_settings
from .utils import save_image, save_image_in_filesystem

router = APIRouter(prefix="/api/medias", tags=["medias"])


@router.post("")
async def create_image_view(
        file: UploadFile,
        request: Request,
        session: AsyncSession = Depends(db_settings.session),
) -> Dict[str, bool | int]:
    user = await get_user_by_api_key(
        session=session, api_key=request.headers.get("api-key")
    )
    if user is None:
        return error_response(msg="неправильный api key", err_type=405)
    name = file.filename
    bytes_ = file.file.read()
    saved_image_data = await save_image(name=name, file=bytes_, session=session)
    id = saved_image_data.get("id")
    await save_image_in_filesystem(name=saved_image_data.get("filename"), saved_file=bytes_)
    return ok_response(resp=id, name="media_id")


@router.get("/{filename}")
async def get_image_view(filename: str):
    image = await get_image(filename=filename)
    return image
