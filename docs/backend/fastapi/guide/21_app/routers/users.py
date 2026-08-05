from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_users_me():
    return {"user_name": "John Doe"}