"""
声明的参数不是路径参数时，路径操作函数会把该参数自动解释为“查询”参数。

查询参数：
- 可选参数：q: str | None = None
- 必选参数：skip: int, limit: int 
- bool参数：active: bool
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/items/")
def search_items(q: str | None = None):
    return {"q": q}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/item/list")
def read_item_list(skip:int, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/users/{user_id}")
def get_active_users(user_id: str, active: bool):
    return {"user_id": user_id, "active": active}