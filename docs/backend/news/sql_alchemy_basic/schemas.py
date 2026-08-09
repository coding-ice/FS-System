
from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    age: int


class CreateUser(BaseUser):
    password: str


class UpdateUser(BaseModel):
    username: str | None = None
    age: int | None = None
    password: str | None = None
