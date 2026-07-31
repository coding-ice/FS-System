from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


app = FastAPI()


class UserIn(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str


# 设置了 response_model 回自动过滤非 response_model 的字段
@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}