from fastapi import APIRouter

from ..deps import DB_DEPS
from ..models import User
from ..schemas import BaseUser, CreateUser

router = APIRouter(tags=["用户创建"])


@router.post("/users", response_model=BaseUser)
async def create_user(user: CreateUser, db: DB_DEPS) -> User:
    new_user = User(**user.model_dump())
    db.add(new_user)
    await db.flush()
    return new_user
