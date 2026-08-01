from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

items = {
    "keyboard": {
        "name": "键盘",
        "description": "机械键盘",
        "price": 100,
        "tax": 9.9,
        "tags": ["office"]
    }
}

class BaseItem(BaseModel):
    description: str | None = None
    tax: float | None = 10
    tags: list[str] = []

class CreateItem(BaseItem):
    name: str
    price: float

class UpdateItem(BaseItem):
    name: str | None = None
    price: float | None = None


# 如果我只想要改一个 price，用了 put 会整个覆盖掉，要么走默认值
@app.put("/items/{item_id}")
async def put_item(item_id: str, item: UpdateItem):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.model_dump()
    return items[item_id]

@app.patch("/items/{item_id}")
async def patch_item(item_id: str, item: UpdateItem):

    # 自己写的
    # if item_id not in items:
    #     raise HTTPException(status_code=404, detail="Item not found")
    # # 过滤掉 None 的值
    # target_item = item.model_dump(exclude_unset=True)
    # # 更新原来的 item
    # original_item = items[item_id]
    # original_item.update(target_item)
    # return original_item

    stoage_item = items.get(item_id)

    if not stoage_item:
        raise HTTPException(status_code=404, detail="Item not found")
    # 1. 创建pydantic模型实例
    new_storage_item = CreateItem(**stoage_item)
    # 2. 更新数据
    update_data = item.model_dump(exclude_unset=True)
    # 3. 更新模型实例
    updated_data = new_storage_item.model_copy(update=update_data)
    # 4. 转换为字典
    items[item_id] = jsonable_encoder(updated_data)

    return updated_data