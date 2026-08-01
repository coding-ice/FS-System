from dataclasses import dataclass
from typing import Annotated, Any
from fastapi import Cookie, Depends, FastAPI, HTTPException, Header


app = FastAPI()

def verify_token(x_token: Annotated[str | None, Header()] = None):
    if not x_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return x_token


# dependencies：是没有返回值的，做前置校验
@app.get("/get_permission", dependencies=[Depends(verify_token)])
def get_products():
    return {"has_permission": True}