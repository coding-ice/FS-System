from typing import Annotated
from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/get_cookie")
async def get_cookie(name: Annotated[str, Cookie()]):
    return {"message": "Hello World"}
