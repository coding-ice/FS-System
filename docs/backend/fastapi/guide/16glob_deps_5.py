
from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Header


def verify_token(x_token: Annotated[str | None, Header()] = None):
    if not x_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return x_token

app = FastAPI()

admin_router = APIRouter(prefix="/admin", dependencies=[Depends(verify_token)])



@admin_router.get("/get_permission")
def get_admin_permission():
    return {"has_permission": True}


app.include_router(admin_router)



@app.get("/get_permission")
def get_permission():
    return {"has_permission": True}