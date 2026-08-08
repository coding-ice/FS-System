from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Demo",
    description="## A simple FastAPI demo \n ### Hi",
    version="0.1.0",
    terms_of_service="https://www.google.com",
    contact={
        "name": "FastAPI Demo",
        "url": "https://www.google.com",
        "email": "test@example.com"
    },
    license={
        "name": "MIT License",
        "url": "https://www.google.com"
    },
    # openapi_url=None
)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}