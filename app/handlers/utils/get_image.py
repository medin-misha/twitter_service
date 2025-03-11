from fastapi import status, HTTPException
import httpx
from io import BytesIO
from starlette.responses import StreamingResponse
from core import config


async def get_image(filename: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(config.image_saver_url + "images/" + filename)
    status_code = response.status_code
    if status_code != 200:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return StreamingResponse(
        iter([response.content]), media_type=f"image/{filename.split('.')[-1]}"
    )
