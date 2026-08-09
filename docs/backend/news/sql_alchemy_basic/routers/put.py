from fastapi import APIRouter, HTTPException

from ..deps import DB_DEPS
from ..models import User
from ..schemas import BaseUser, UpdateUser

router = APIRouter(tags=["用户更新"])

@router.put("/users/{user_id}", response_model=BaseUser)
async def update_user(user_id: int, user: UpdateUser, db: DB_DEPS) -> User:
    db_user = await db.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="用户不存在")

    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
        
    return db_user