import time
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_log(email: str, msg):
    time.sleep(10)
    with open("log.txt", "a") as f:
        f.write(f"{email}: {msg}\n")

@app.post("/notice_event/{email}")
async def notice_event(email: str, BackgroundTasks: BackgroundTasks):
    BackgroundTasks.add_task(write_log, email, "Event triggered")
    return {"message": "Event triggered"}