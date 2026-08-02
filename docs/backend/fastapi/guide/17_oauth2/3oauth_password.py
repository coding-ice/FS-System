from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "ice": {
        "username": "ice",
        "full_name": "Ice",
        "email": "ice@example.com",
        "disabled": False,
        "hashed_password": "fakehashed123456",
    },
}

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool = False

class UserInDB(User):
    hashed_password: str


def fake_hash_password(password: str):
    return "fakehashed" + password

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if form_data.username not in fake_users_db:
        raise HTTPException(status_code=401, detail="用户不存在")

    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == fake_users_db[form_data.username]["hashed_password"]:
        raise HTTPException(status_code=401, detail="密码错误")
    
    return {"access_token": form_data.username, "token_type": "bearer"}

def get_user(username: str):
    user = fake_users_db.get(username)
    return UserInDB(**user) if user else None

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="无效的 token")
    return user

def get_current_active_user(current_user: Annotated[UserInDB, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.get("/users/me")
async def read_users_me(user: Annotated[User, Depends(get_current_active_user)]):
    return {"user": user}