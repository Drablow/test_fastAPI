from fastapi import APIRouter, Depends
from typing import Annotated
from repository.user_repository import UserRepository
from schemas import SUserCreate, SUser, SUserId

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.post("")
async def add_user(
        user: Annotated[SUserCreate, Depends()]
) -> SUserId:
    user_id = await UserRepository.add_one(user)
    return {"ok": True, "user_id": user_id}


@router.get("")
async def get_user() -> list[SUser]:
    users = await UserRepository.get_all()
    return users

