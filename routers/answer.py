from fastapi import APIRouter
from deta import Deta
from models.answer import *
from utills import *

from database import answer_db as db

router = APIRouter(prefix='/answer', tags=["Answer"])


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


@router.put("/")
async def update_answer(update: Answer_update, id: str):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=id)
    return True


@router.delete("/{id}")
async def delete_answer(id: str):
    db.delete(key=id)
    return True
