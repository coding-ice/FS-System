from dataclasses import dataclass
from typing import Annotated, Any
from fastapi import Cookie, Depends, FastAPI


app = FastAPI()

def get_query(q: str | None = None):
    return q


def get_last_query(q: Annotated[str, Depends(get_query)], last_query: Annotated[str | None, Cookie()] = None):
    return q or last_query

@app.get("/products")
async def get_products(q: Annotated[str, Depends(get_last_query)]):
    return {"q": q}
