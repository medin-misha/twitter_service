from httpx import Response, AsyncClient, ASGITransport
import pytest_asyncio
from typing import Dict
import random
import main


async def user(client: AsyncClient) -> Response:
    user_creating = {"name": "misha", "key": f"{random.randint(10 ** 10, 10 ** 12)}"}

    user_create: Response = await client.post(url="api/users/", json=user_creating)

    assert user_create.status_code == 200
    assert user_create.json().get("result") is True
    assert user_create.json().get("user").get("key") == user_creating.get("key")

    return user_create


async def image(client: AsyncClient, api_key: str) -> Response:
    img_response: Response = await client.post(
        url="/api/medias",
        headers={"api-key": api_key},
        files={
            "file": (
                "anime.jpg",
                (
                    open(
                        "tests/imgs/anime.jpg",
                        "rb",
                    )
                ),
            )
        },
    )
    assert img_response.status_code == 200
    assert img_response.json().get("result") is True
    assert isinstance(img_response.json().get("media_id"), int)

    return img_response


async def tweet(client: AsyncClient, api_key: str, image_id: int) -> Response:
    tweet_response: Response = await client.post(
        url="api/tweets",
        headers={"api-key": f"{api_key}"},
        json={"tweet_data": "ААААниме", "tweet_media_ids": [image_id]},
    )
    assert tweet_response.status_code == 200
    assert tweet_response.json().get("result") is True
    assert isinstance(tweet_response.json().get("tweet_id"), int)

    return tweet_response


async def models() -> Dict[str, Response]:
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        user_creating = await user(client=client)
        image_creating = await image(
            client=client, api_key=user_creating.json().get("user").get("key")
        )
        tweet_creating = await tweet(
            client=client,
            api_key=user_creating.json().get("user").get("key"),
            image_id=image_creating.json().get("media_id"),
        )
    return {
        "user": user_creating,
        "image": image_creating,
        "tweet": tweet_creating,
        "api_key": user_creating.json().get("user").get("key"),
    }
