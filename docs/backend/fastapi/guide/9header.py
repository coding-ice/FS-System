from typing import Annotated
from fastapi import FastAPI, Header


app = FastAPI()

# convert_underscores：是否将下划线转换为连字符
"""
user_agent（转换） -> 实际取值的是浏览器中的 User-Agent
"""
@app.get("/get_header")
async def get_header(user_agent: Annotated[str | None, Header()]):
    return {"user_agent": user_agent}

@app.get("/get_token")
async def get_token(token: Annotated[list[str] | None, Header()]):
    return {"token": token}