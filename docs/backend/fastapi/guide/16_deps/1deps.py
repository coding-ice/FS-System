from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()

def common_params(q: str = '',limit: int = 10, offset: int = 0):
    return {"q": q, "limit": limit, "offset": offset}

CommonParams = Annotated[dict, Depends(common_params)]

@app.get("/users")
async def get_users(params: CommonParams):
    return {"data": "users", "params": params}