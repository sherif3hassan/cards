from fastapi import APIRouter
from deta import Deta
from models.answer import *
from schemas.answer import Answer_schema
from utills import *

from database import OUR_DETA_PROJECT_KEY
deta = Deta(OUR_DETA_PROJECT_KEY)

router = APIRouter(prefix='/answer', tags=["Answer"])
db = deta.Base("answer_db")


@router.post("/")
async def create_answer(answer: Answer):
    db.insert(answer.dict())
    return answer


@router.get("/{id}")
async def get_answer(id: str):
    return db.get(key=id)


@router.get("/")
async def get_all_answer():
    return db.fetch().items


@router.put("/{key}")
async def update_answer(update: Answer_schema, key: str):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=key)
    return True


@router.delete("/{id}")
async def delete_answer(id: str):
    db.delete(key=id)
    return True
