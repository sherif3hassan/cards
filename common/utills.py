
from fastapi import Depends, HTTPException, status
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decode_jwt
from pydantic import BaseModel


def clean_dict(update: dict):
    update_dict = {
        key: value
        for key, value in zip(update.keys(), update.values())
        if value is not None
    }
    return update_dict


class TokenData(BaseModel):
    username: str
    room_id: str


def get_token_data(token=Depends(JWTBearer)) -> TokenData:
    data = decode_jwt(token)
    
    if data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return TokenData(username=data["username"], room_id=data["room_id"])
