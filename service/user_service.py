from typing import List, Optional

from api import poll_service_api
from model.user import User
from model.user_request import UserRequest
from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)


async def get_user_by_email(email: str) -> Optional[User]:
    return await user_repository.get_user_by_email(email)


async def get_all_users() -> List[User]:
    return await user_repository.get_all_users()


async def create_user(user: UserRequest) -> int:
    return await user_repository.create_user(user)


async def update_user(user_id: int, user: UserRequest):
    await user_repository.update_user(user_id, user)


async def register_user(user_id: int):
    await user_repository.register_user(user_id)


async def delete_user_by_id(user_id: int):
    # The answers live in the poll service, so they are removed first through its API.
    # If the poll service can't be reached the user is kept, so no orphan answers are left behind.
    await poll_service_api.delete_user_answers(user_id)
    await user_repository.delete_user_by_id(user_id)
