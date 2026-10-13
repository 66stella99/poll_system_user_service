import httpx

from repository.database import config


async def delete_user_answers(user_id: int):
    url = f"{config.POLL_SERVICE_URL}/answer/user/{user_id}"
    async with httpx.AsyncClient() as client:
        await client.delete(url)
