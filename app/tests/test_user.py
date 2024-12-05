from httpx import Response, AsyncClient, ASGITransport
import main
from .fixtures import models


async def test_get_users_list():
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get("api/users/")
        assert response.status_code == 200
        assert isinstance(response.json().get("users"), list)
        assert response.json().get("result") is True


# user me
async def test_get_users_me():
    model_data = await models()
    headers = {"api-key": model_data.get("user").json().get("user").get("key")}
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get("api/users/me", headers=headers)
        assert response.status_code == 200
        assert response.json().get("result") is True
        assert response.json().get("user").get("id") is not None


async def test_auth_err_get_users_me():
    model_data = await models()
    headers = {"api-key": "a"}
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get("api/users/me", headers=headers)
        assert response.status_code == 401
        assert response.json().get("result") is False


# user id
async def test_users_get_id():
    model_data = await models()
    user_id = model_data.get("user").json().get("user").get("id")
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get(f"api/users/{user_id}")
        assert response.status_code == 200
        assert response.json().get("result") is True
        assert response.json().get("user").get("id") is not None


async def test_not_found_users_get_id():
    model_data = await models()
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.get(f"api/users/{10 ** 3}")
        assert response.status_code == 404
        assert response.json().get("result") is False
        assert response.json().get("user") is None


# user delete
async def test_delete_user_by_id():
    model_data = await models()
    user_id = model_data.get("user").json().get("user").get("id")
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        response: Response = await client.delete(f"api/users/{user_id}")
        assert response.status_code == 200
        user_get: Response = await client.get(f"api/users/{user_id}")
        assert user_get.status_code == 404


# user follow
async def test_follow_user():
    model_data = await models()
    user_key = model_data.get("user").json().get("user").get("key")
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test/"
    ) as client:
        followed_user: Response = await client.get("api/users/")
        users_count = len(followed_user.json().get("users"))

        assert len(followed_user.json().get("users")) > 1

        user_id = followed_user.json().get("users")[users_count - 1].get("id")
        follower: Response = await client.post(
            f"api/users/{user_id}/follow", headers={"api-key": user_key}
        )

        assert follower.status_code == 200
        assert follower.json().get("result") is True

        unfollower: Response = await client.delete(
            f"api/users/{user_id}/follow", headers={"api-key": user_key}
        )
        assert unfollower.status_code == 200
        assert unfollower.json().get("result") is False
