from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
import jwt
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError


SECRET_KEY = "qwerDF123.."
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()
scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

fake_users_db = {
    "ice": {
        "username": "ice",
        "hashed_password": password_hash.hash("123456"),
    }
}


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not password_hash.verify(password, user["hashed_password"]):
        return 
    return UserInDB(**user)

def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        'sub': subject,
        'exp': expire,
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    return Token(access_token=create_access_token(user.username), token_type="bearer")

def get_current_user(token: Annotated[str, Depends(scheme)]):
    CredentialsError = HTTPException(status_code=401, detail="无效的 token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username or not isinstance(username, str):
            raise CredentialsError
    except InvalidTokenError:
        raise CredentialsError

    user = fake_users_db.get(username)
    if not user:
        raise CredentialsError
    return UserInDB(**user)

@app.get("/users/me", response_model=User)
async def read_users_me(user: Annotated[UserInDB, Depends(get_current_user)]):
    return user