from contextlib import asynccontextmanager
from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 1. 创建异步引擎
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/fastapi_first"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL, echo=True, pool_size=10, max_overflow=20
)


def utcnow() -> datetime:
    return datetime.now(UTC)


class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(default=utcnow)
    update_time: Mapped[datetime] = mapped_column(
        default=utcnow,
        onupdate=utcnow,
    )


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await async_engine.dispose()


app = FastAPI(lifespan=lifespan)


AsyncSessionLocal = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

DB_DEPS = Annotated[AsyncSession, Depends(get_db)]

@app.get("/users")
async def get_users(db: DB_DEPS):
    # result = await db.execute(select(User))
    # 获取所有数据
    # users = result.scalars().all()
    # 单条数据
    # user = result.scalars().first()
    # 通过主键获取单条

    # 通过主键获取单条
    user = await db.get(User, 1)

    return user

user_ids = [1,2]


# @app.get("/users/list")
# async def get_users_list(db: DB_DEPS, offset: int = 0, limit: int = 10):
#     result = await db.execute(select(User).offset(offset).limit(limit))
#     return result.scalars().all()


@app.get("/users/count")
async def get_users_count(db: DB_DEPS):
    # result = await db.execute(select(func.count(User.id)))
    # return {
    #     "total": result.scalar()
    # }

    # result = await db.execute(select(func.avg(User.age)))
    # return {
    #     "age": result.scalar()
    # }

    result = await db.execute(select(func.min(User.age)))
    return {
        "min": result.scalar()
    }


@app.get("/users/list")
async def get_users_list(db: DB_DEPS, page: int = 0, page_size: int = 10):
    result = await db.execute(select(User).offset(page * page_size).limit(page_size))
    return result.scalars().all()


# 模糊查询 与非 in 
@app.get("/users/like_username")
async def get_users_like_username(username: str, db: DB_DEPS):
    # % 模糊查询 0/1多个
    # result = await db.execute(select(User).where(User.username.like(f"{username}%")))
    # return result.scalars().all()

    # 单个占位
    # result = await db.execute(select(User).where(User.username.like(f"{username}_")))
    # return result.scalars().all()

    # result = await db.execute(select(User).where(User.username.like(f"{username}%") & (User.age > 18)))
    # result = await db.execute(select(User).where(User.username.like(f"{username}%") | (User.age > 18)))
    # return result.scalars().all()

    # in 查询
    result = await db.execute(select(User).where(User.id.in_(user_ids)))
    return result.scalars().all()


# 查询年龄 > 18 的数据
@app.get("/users/age_gt_18")
async def get_users_age_gt_18(db: DB_DEPS):
    result = await db.execute(select(User).where(User.age > 18))
    return result.scalars().all()


@app.get("/users/{user_id}")
async def get_user(user_id:int, db: DB_DEPS):
    # user = await db.get(User, user_id)
    # return user

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    return user

