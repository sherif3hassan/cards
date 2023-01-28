from fastapi import APIRouter, Depends

from common.utills import clean_dict
from database import get_question_db
from models.question import Question
from schemas.question import Question_schema

router = APIRouter(prefix="/question", tags=["Question"])


@router.get("/")
def get_all_questions(db=Depends(get_question_db)):
    res = db.fetch()
    return res.items


@router.get("/{key}")
def get_question(key: str, db=Depends(get_question_db)):
    return db.get(key)


@router.post("/")
def create_question(question: Question, db=Depends(get_question_db)):
    res = db.insert(question.dict())
    return res


@router.put("/{key}")
def update_question(
    update_question: Question_schema, key: str, db=Depends(get_question_db)
):
    update_dict = clean_dict(update_question.dict())
    db.update(updates=update_dict, key=key)
    return True


@router.delete("/{key}")
def delete_question(key: str, db=Depends(get_question_db)):
    deleted = db.get(key)
    db.delete(key)
    return deleted
