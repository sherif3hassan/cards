from fastapi import APIRouter
from models.question import Question
from database import question_db as db
from schemas.question import Question_schema
from utills import clean_dict

router = APIRouter(prefix="/question", tags=["Question"])


@router.get("/")
def get_all_questions():
    res = db.fetch()
    return res.items


@router.get("/{key}")
def get_question(key: str):
    return db.get(key)


@router.post("/")
def create_question(question: Question):
    res = db.insert(question.dict())
    return res


@router.put("/{key}")
def update_question(update_question: Question_schema, key: str):
    update_dict = clean_dict(update_question.dict())
    db.update(updates=update_dict, key=key)
    return True


@router.delete("/{key}")
def delete_question(key: str):
    deleted = db.get(key)
    db.delete(key)
    return deleted
