from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()


@dataclass
class CommonParamsClass:
    keywords: str = ''
    limit: int = 10
    offset: int = 0

"""
1. fastapi 调用 CommonParamsClass 的实例化方法，并返回一个 CommonParamsClass 实例
2. 该实例为 params 的依赖注入参数

可以简写，Annotated[CommonParamsClass, Depends()]
因为 CommonParamsClass 本身是一个类知道如何调用
"""
CommonParams = Annotated[CommonParamsClass, Depends()]

@app.get("/users")
async def get_users(params: CommonParams):
    return {"data": "users", "params": params}