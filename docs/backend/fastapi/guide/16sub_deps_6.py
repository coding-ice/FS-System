
from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Header


app = FastAPI()

class Cls_C:
    def __init__(self, name: str):
        print("Initializing C")
        self.name = name

    def close(self):
        print("Closing C")

class Cls_B:
    def __init__(self, name: str):
        print("Initializing B")
        self.name = name

    def close(self):
        print("Closing B")

def get_b():
    b = Cls_B(name="b")
    try:
        yield b
    finally:
        b.close()

B = Annotated[Cls_B, Depends(get_b)]


def get_c(b: B):
    c = Cls_C(name="c")
    try:
        yield c
    finally:
        c.close()

C = Annotated[Cls_C, Depends(get_c)]

@app.get("/items")
def read_items(c: C):
    return {"message": "Items are here"}