from httpx import Response, AsyncClient, ASGITransport
import main
from .fixtures import models


async def test_get_tweet_list():
    model_data = await models()
    headers = {"api-key": model_data.get("user").json().get("user").get("key")}
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get("api/tweets")
        assert response.status_code == 200
        assert response.json().get("result") is True
        assert isinstance(response.json().get("tweets"), list)


async def test_delete_tweet():
    model_data = await models()
    headers = {"api-key": model_data.get("api_key")}
    tweet_id = model_data.get("tweet").json().get("tweet_id")
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        deleted_tweet: Response = await client.delete(
            f"api/tweets/{tweet_id}", headers=headers
        )
        assert deleted_tweet.status_code == 200
        assert deleted_tweet.json().get("result") is True


async def test_like_tweet():
    model_data = await models()
    headers = {"api-key": model_data.get("user").json().get("user").get("key")}
    tweet_id = model_data.get("tweet").json().get("tweet_id")
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        liked: Response = await client.post(
            f"api/tweets/{tweet_id}/likes", headers=headers
        )
        del_like: Response = await client.delete(
            f"api/tweets/{tweet_id}/likes", headers=headers
        )

        assert liked.status_code == 200
        assert liked.json().get("result") is True

        assert del_like.status_code == 200
        assert del_like.json().get("result") is False
