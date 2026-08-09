from contextlib import asynccontextmanager

from fastapi import FastAPI

from .deps import async_engine
from .models import Base
from .routers import create, put, select


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await async_engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(create.router)
app.include_router(select.router)
app.include_router(put.router)
