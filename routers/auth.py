from fastapi import APIRouter, Depends
from auth.auth_handler import sign_jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from auth.auth_handler import decode_jwt
from fastapi import Depends, HTTPException, status

router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

class TokenData(BaseModel):
    username: str
    room_id: str

@router.post("/")
async def create_token(body: OAuth2PasswordRequestForm = Depends()):
    return sign_jwt({"username": body.username, "room_id": body.password})

def get_token_data(token: str = Depends(oauth2_scheme)) -> TokenData:
    data = decode_jwt(token)
    
    if data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return TokenData(username=data["username"], room_id=data["room_id"])
