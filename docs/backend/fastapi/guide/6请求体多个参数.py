from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

class User(BaseModel):
    name: str = Field(default="John Doe")
    age: int
    email: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 多个 pydantic，入参需要包含 key
# @app.post("/items")
# async def create_item(user: User, item: Item):
#     return {"user": user, "item": item}

@app.post("/items")
async def create_item(user: Annotated[User, Body(embed=True)]):
    return {"user": user}



@app.put("/items/{item_id}")
async def update_item(item_id: int, importance: Annotated[int, Body()]):
    return {"item_id": item_id, "importance": importance}