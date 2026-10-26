import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextStreamResponse(StreamingResponse):
    media_type = "text/event-stream"



@app.get("/reply", response_class=TextStreamResponse)
async def reply(message: str):
    for i in range(10):
        yield f"message: {message} {i}\n"
        await asyncio.sleep(1)


