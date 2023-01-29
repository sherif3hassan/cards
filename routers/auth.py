from fastapi import APIRouter
from auth.auth_handler import sign_jwt

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/")
async def create_token(username: str, room_id: str):
    return sign_jwt({"username": username, "room_id": room_id})
