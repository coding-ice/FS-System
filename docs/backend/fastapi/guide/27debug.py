from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def sum(a: int, b: int):
    print(a, b)
    total = a + b

    return total


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)