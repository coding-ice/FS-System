from typing import Annotated
from fastapi import Depends, HTTPException, Header


def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "dev-secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")

    return x_token

TokenDeps = Annotated[str, Depends(verify_token)]

