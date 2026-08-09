from fastapi import APIRouter
from sqlalchemy import func, select

from ..deps import DB_DEPS
from ..models import User

router = APIRouter(tags=["用户查询"])

USER_IDS = [1, 2]


@router.get("/users/count")
async def get_users_count(db: DB_DEPS) -> dict[str, int | None]:
    result = await db.execute(select(func.min(User.age)))
    return {"min": result.scalar()}


@router.get("/users/list")
async def get_users_list(
    db: DB_DEPS,
    page: int = 0,
    page_size: int = 10,
):
    result = await db.execute(
        select(User).offset(page * page_size).limit(page_size)
    )
    return list(result.scalars().all())


@router.get("/users/like_username")
async def get_users_like_username(username: str, db: DB_DEPS):
    _ = username
    result = await db.execute(select(User).where(User.id.in_(USER_IDS)))
    return list(result.scalars().all())


@router.get("/users/age_gt_18")
async def get_users_age_gt_18(db: DB_DEPS):
    result = await db.execute(select(User).where(User.age > 18))
    return list(result.scalars().all())


@router.get("/users/{user_id}")
async def get_user(user_id: int, db: DB_DEPS):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
