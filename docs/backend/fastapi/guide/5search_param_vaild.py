from typing import Annotated
from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/items")
def search_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    print('--------------------------------')
    print(Annotated[str | None, Query(min_length=3, max_length=50)])
    print('--------------------------------')

    data = {"items": [{'item_id': 1}, {'item_id': 2}]}
    if q:
        data.update({"q": q})
    return data


@app.get("/users")
def get_users(q: Annotated[list[str], Query(min_length=1)]):
    return {"q": q}