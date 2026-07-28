from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class OrderStatus(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@app.get("/orders/{order_status}")
def get_order(order_status: OrderStatus): # 值为 enum 的 value
    print(order_status)
    print(order_status.value)
    return {"order_status": order_status}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}