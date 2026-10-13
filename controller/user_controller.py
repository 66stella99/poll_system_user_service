from typing import List

from fastapi import APIRouter, HTTPException, status

from model.user import User
from model.user_request import UserRequest
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/", response_model=List[User])
async def get_users():
    return await user_service.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
    return user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest):
    if await user_service.get_user_by_email(user.email):
        raise HTTPException(status_code=409, detail=f"User with email: {user.email} already exists")
    user_id = await user_service.create_user(user)
    return await user_service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserRequest):
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail=f"Can't update user with id: {user_id}, user not found")
    user_with_same_email = await user_service.get_user_by_email(user.email)
    if user_with_same_email and user_with_same_email.id != user_id:
        raise HTTPException(status_code=409, detail=f"User with email: {user.email} already exists")
    await user_service.update_user(user_id, user)
    return await user_service.get_user_by_id(user_id)


@router.put("/{user_id}/register", response_model=User)
async def register_user(user_id: int):
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail=f"Can't register user with id: {user_id}, user not found")
    if existing_user.is_registered:
        raise HTTPException(status_code=409, detail=f"User with id: {user_id} is already registered")
    await user_service.register_user(user_id)
    return await user_service.get_user_by_id(user_id)


@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
    await user_service.delete_user_by_id(user_id)
    return existing_user
