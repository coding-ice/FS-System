from contextlib import asynccontextmanager
from typing import Annotated
import uuid
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine, Field, select


engine = create_engine("sqlite:///sqlite.db", connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

class BaseHero(SQLModel):
    name: str
    age: int

class Hero(BaseHero, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    secret_name: str | None = Field(default=None) # 不返回给前端

class CreateHero(BaseHero):
    pass

class UpdateHero(SQLModel):
    name: str | None = None
    age: int | None = None

class HeroPublic(BaseHero):
    id: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

SessionDeps = Annotated[Session, Depends(get_session)]

@app.post("/heroes", response_model=HeroPublic)
async def create_hero(hero: CreateHero, session: SessionDeps):
    hero_data = Hero.model_validate(hero)
    session.add(hero_data)
    session.commit()
    session.refresh(hero_data)

    return hero_data

@app.get("/heroes", response_model=list[HeroPublic])
async def get_heroes(session: SessionDeps, offset: int = 0, limit: int = 10):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get("/heroes/{hero_id}", response_model=HeroPublic)
async def get_hero(hero_id: str, session: SessionDeps):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
async def update_hero(hero_id: str, data: UpdateHero, session: SessionDeps):
    # 1. 获取数据
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@app.delete("/heroes/{hero_id}")
async def delete_hero(hero_id: str, session: SessionDeps):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"deleted": True}