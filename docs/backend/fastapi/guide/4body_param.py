from dataclasses import dataclass
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: str
    price: float
    tax: float | None


@app.post("/items")
def create_item(item: Item):
    item_dict = item.model_dump_json()
    print(item_dict)

    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id,  **item.model_dump()}