from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


items = {"keyboard": "hhh", "mouse": "kkk"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=200, detail={"code": 404, "message": "Item not found"})
    return {"item": items[item_id]}


class Insufficient_Balance(Exception):
    def __init__(self, balance: int, required: int):
        self.balance = balance
        self.required = required


@app.exception_handler(Insufficient_Balance)
def insufficient_balance_handler(request: Request, exc: Insufficient_Balance):
    return JSONResponse(status_code=200, content={"code": 400, "message": "Insufficient balance", "data": {"balance": exc.balance, "required": exc.required}})

@app.post("/buy_item")
async def buy_item():
    price = 100
    balance = 50
    if balance < price:
        raise Insufficient_Balance(balance=balance, required=price)

    return {"success": True}


# 这个非常重要，一定会用到
@app.exception_handler(RequestValidationError)
def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        errors.append({
            "type": error["type"],
            "msg": error["msg"],
            "loc": ".".join(error["loc"]),
        })

    return JSONResponse(status_code=200, content={"code": 400, "message": "参数校验失败", "errors": errors})

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}


@app.exception_handler(StarletteHTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=200, content={"code": exc.status_code, "message": exc.detail})


@app.get("/products/{product_id}")
async def get_products(product_id: int):
    if product_id < 0:
        raise HTTPException(status_code=200, detail="Product ID must be positive")
    return {"product_id": product_id}