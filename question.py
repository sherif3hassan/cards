from fastapi import APIRouter
from deta import Deta

from models.question import Question

router = APIRouter(prefix="/question")

deta = Deta("a0t0pjsh_PrZdmxu7pwZHGJPuGsjw6JhpbbF9Ggfh")

db = deta.Base("/question")


@router.get("/")
def get_all_questions():
    return db.fetch().items


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
