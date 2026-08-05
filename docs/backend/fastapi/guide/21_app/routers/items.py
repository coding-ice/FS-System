from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import verify_token

items = {
    "keyboard": {
        "name": "Keyboard",
        "price": 100,
        "description": "A keyboard is a device that allows you to type text and commands into a computer or other device."
    },
    "mouse": {
        "name": "Mouse",
        "price": 50,
        "description": "A mouse is a device that allows you to control the cursor on a computer screen."
    }
}

router = APIRouter(prefix="/items", tags=["items"], dependencies=[Depends(verify_token)])

@router.get("/")
async def read_items():
    return items

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]