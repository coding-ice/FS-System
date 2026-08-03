from fastapi import FastAPI, Request, Response
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

app = FastAPI()

class Middleware1(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print("Middleware 1")
        response = await call_next(request)
        print("Middleware 1 after")
        return response

class Middleware2(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print("Middleware 2")
        response = await call_next(request)
        print("Middleware 2 after")
        return response


app.add_middleware(Middleware1)
app.add_middleware(Middleware2)

"""
打印结果
Middleware 2
Middleware 1
router called
Middleware 1 after
Middleware 2 after


"""


@app.get("/")
async def root():
    print("router called")
    return {"message": "Hello, World!"}