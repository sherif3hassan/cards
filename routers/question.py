from fastapi import APIRouter

from models.question import Question

from database import question_db as db

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
def update_question(key: str, question: dict):
    db.put(question, key)
    return db.get(key)


@router.delete("/{key}")
def delete_question(key: str):
    deleted = db.get(key)
    db.delete(key)
    return deleted
