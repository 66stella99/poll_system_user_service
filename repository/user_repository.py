from typing import List, Optional

from model.user import User
from model.user_request import UserRequest
from repository.database import database

TABLE_NAME = "users"


async def get_user_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id = :user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return User(**result._mapping)
    return None


async def get_user_by_email(email: str) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE email = :email"
    result = await database.fetch_one(query, values={"email": email})
    if result:
        return User(**result._mapping)
    return None


async def get_all_users() -> List[User]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [User(**result._mapping) for result in results]


async def create_user(user: UserRequest) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, email, age, address, joining_date)
        VALUES (:first_name, :last_name, :email, :age, :address, :joining_date)
    """
    return await database.execute(query, values=user.model_dump())


async def update_user(user_id: int, user: UserRequest):
    query = f"""
        UPDATE {TABLE_NAME}
        SET first_name = :first_name,
            last_name = :last_name,
            email = :email,
            age = :age,
            address = :address,
            joining_date = :joining_date
        WHERE id = :user_id
    """
    await database.execute(query, values={**user.model_dump(), "user_id": user_id})


async def register_user(user_id: int):
    query = f"UPDATE {TABLE_NAME} SET is_registered = TRUE WHERE id = :user_id"
    await database.execute(query, values={"user_id": user_id})


async def delete_user_by_id(user_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :user_id"
    await database.execute(query, values={"user_id": user_id})
