from fastapi import APIRouter, Depends

from auth.auth_bearer import JWTBearer
from auth.auth_handler import sign_jwt

router = APIRouter(prefix="/example", tags=["JWT example"])


@router.post("/")
async def create_token(username: str):
    return sign_jwt({"username": username})


@router.get("/")
async def get_secret(token=Depends(JWTBearer())):
    return {"secret": "im potato"}
