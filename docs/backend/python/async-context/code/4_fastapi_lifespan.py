import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request


class EmailClient:
    async def connect(self) -> None:
        await asyncio.sleep(0.1)
        print("邮件客户端已连接")

    async def close(self) -> None:
        await asyncio.sleep(0.1)
        print("邮件客户端已关闭")

    async def send(self, address: str) -> None:
        print(f"向 {address} 发送邮件")


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = EmailClient()
    await client.connect()  # 应用开始接收请求前执行一次
    app.state.email_client = client

    try:
        yield
    finally:
        await client.close()  # 应用停止时执行一次


app = FastAPI(lifespan=lifespan)


@app.post("/emails/{address}")
async def send_email(address: str, request: Request):
    await request.app.state.email_client.send(address)
    return {"message": "已提交发送任务"}
