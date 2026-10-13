import httpx
from fastapi import HTTPException

from config.config import config


async def delete_user_answers(user_id: int):
    url = f"{config.POLL_SERVICE_URL}/answer/user/{user_id}"
    try:
        async with httpx.AsyncClient(timeout=config.HTTP_TIMEOUT_SECONDS) as client:
            response = await client.delete(url)
            response.raise_for_status()
    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail=f"Poll service is unavailable, can't delete the answers of user with id: {user_id}"
        )
