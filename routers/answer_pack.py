from deta import Deta  # Import Deta
from fastapi import APIRouter
from models.answerpack import *
from database import answerpack_db as db
from schemas.answer_pack import AnswerPack_schema
from utills import clean_dict



router = APIRouter(prefix='/answerpack', tags=["Answer Pack"])

@router.post("/")
def create_answerpack(answer_pack: AnswerPack):
    db.insert(answer_pack.dict())
    return True


@router.get("/{id}")
def get_answer(id: str):
    return db.get(key=id)


@router.get("/")
def get_all_answer_packs():
    res = db.fetch()
    return res.items


@router.put("/{key}")
def update_answer_pack(update: AnswerPack_schema, key: str):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=key)
    return True


@router.delete("/")
def delete_answer_pack(id: str):
    db.delete(key=id)
    return True
