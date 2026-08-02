from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool = False

fake_users_db = {
    "ice": {
        "username": "ice",
        "full_name": "Ice",
        "email": "ice@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
}

def get_user(username: str):
    if username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**fake_users_db[username])

@app.get("/users/me")
def read_user(token: Annotated[str, Depends(oauth2_schema)]):
    return get_user(token)