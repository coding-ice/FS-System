from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel


class Tag(str, Enum):
    products = "products"
    users = "users"

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

@app.post("/products", tags=[Tag.products], 
status_code=status.HTTP_201_CREATED, summary="创建商品", response_description="新创建的商品", deprecated=True)
async def create_product(product: Product):
    """
    创建一件商品。

    - **name**：商品名称
    - **price**：商品单价，必须大于 0
    """
    return product