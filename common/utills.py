from fastapi import Depends
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decode_jwt
def clean_dict(update: dict):
    update_dict = {
        key: value for key, value in zip(update.keys(), update.values()) if value is not None
    }
    return update_dict

def get_player(token = Depends(JWTBearer)):
    data = decode_jwt(token)
    return data

    