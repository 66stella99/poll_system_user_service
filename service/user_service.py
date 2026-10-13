from typing import Optional, List

from api import poll_service_api
from model.user import User
from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)


async def get_all_users() -> List[User]:
    return await user_repository.get_all_users()


async def create_user(user: User) -> int:
    return await user_repository.create_user(user)


async def update_user(user_id: int, user: User):
    await user_repository.update_user(user_id, user)


async def register_user(user_id: int):
    await user_repository.register_user(user_id)


async def delete_user_by_id(user_id: int):
    # the user's answers are saved in the poll service, so we ask it to delete them
    await poll_service_api.delete_user_answers(user_id)
    await user_repository.delete_user_by_id(user_id)
