from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/me")
def read_me(token: Annotated[str, Depends(oauth2_schema)]):
    return {"token": token}