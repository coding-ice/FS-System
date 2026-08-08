from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


STATIC = Path(__file__).parent / "static"

app = FastAPI()


app.mount("/static", StaticFiles(directory=STATIC), name="static")