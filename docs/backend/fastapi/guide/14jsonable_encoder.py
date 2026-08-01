from datetime import datetime
import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    date: datetime


# pydantic(jsonable_encoder) -> dict -> json.dumps -> str

@app.post("/item")
async def create_item(item: Item):
    item_dict = jsonable_encoder(item)
    print(type(item_dict))
    print(type(json.dumps(item_dict)))
    # print(type(json.du))

    return item # 返回值的时候，fastapi会自动将item转换为json