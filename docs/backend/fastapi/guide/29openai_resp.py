from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    desc: str

class NotFoundResponse(BaseModel):
    detail: str = "Item not found"
    status_code: int = 404

@app.get("/item/{item_id}", response_model=Item, responses={404: {"model": NotFoundResponse}})
async def read_item(item_id: int):
    if item_id == 1:
        return Item(name="Item 1", desc="Item 1 description")
    else:
        error = NotFoundResponse(detail="Item not found", status_code=404)
        return JSONResponse(status_code=error.status_code, content=error.model_dump())