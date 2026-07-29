from fastapi import FastAPI
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(examples=["Foo", "Bar"])
    description: str | None
    price: float
    tax: float | None = None
    
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #                 "hhh": "123"
    #             }
    #         ]
    #     }
    # }
    


app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item