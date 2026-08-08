from fastapi import APIRouter, FastAPI
from pathlib import Path


app = FastAPI()
router = APIRouter()

HERE = Path(__file__).parent
DIST = HERE / "dist"

# app.frontend("/", directory=DIST, fallback="index.html")
router.frontend("/", directory=DIST, fallback="index.html")

app.include_router(router, prefix="/app")

