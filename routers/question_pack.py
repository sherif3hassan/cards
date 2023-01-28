from fastapi import APIRouter, Depends

from database import get_questionpack_db
from models.questionPack import QuestionPack
from schemas.question_pack import QuestionPack_schema
from common.utills import clean_dict

router = APIRouter(prefix="/questionpack", tags=["Question Pack"])


@router.post("/")
def create_question_pack(questionPack: QuestionPack, db=Depends(get_questionpack_db)):
    db.insert(questionPack.dict())
    return True


# get a specific questionpack with a specific ID
@router.get("/{id}")
def get_question_pack(id: str, db=Depends(get_questionpack_db)):
    pack = db.get(key=id)
    return pack


# retreving all data
@router.get("/")
def get_all_question_pack(db=Depends(get_questionpack_db)):
    res = db.fetch()
    return res.items


# update a Question Pack
@router.put("/{key}")
def update_question_pack(
    update: QuestionPack_schema, key: str, db=Depends(get_questionpack_db)
):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=key)
    return True


# Delete a question Pack
@router.delete("/{id}")
def delete_question_pack(id: str, db=Depends(get_questionpack_db)):
    db.delete(key=id)
    return True
