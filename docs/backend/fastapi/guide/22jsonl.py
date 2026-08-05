import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(middleware=[
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
])

class Msg(BaseModel):
    idx: int
    content: str

msg = ["hi", "fastapi", "is", "great"]

@app.get("/messages/stream")
async def stream_messages(): 
    for idx, content in enumerate(msg):
        yield Msg(idx=idx, content=content)
        await asyncio.sleep(1)
