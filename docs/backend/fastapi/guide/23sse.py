import asyncio
from fastapi import FastAPI
from fastapi.sse import EventSourceResponse, ServerSentEvent
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/events", response_class=EventSourceResponse)
async def stream_events():
    yield ServerSentEvent(comment="连接已建立！")

    for i in range(5):
        yield ServerSentEvent(data={"data": f"消息{i}", "index": i}, 
                              event="update", id=f"message-{i}", 
                              retry=3000, comment=f"消息{i}")
        await asyncio.sleep(1)

    yield ServerSentEvent(raw_data="[DONE]", event="done")