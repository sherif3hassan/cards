from deta import Deta
from fastapi import APIRouter
from models.questionPack import QuestionPack
from database import questionpack_db as db
from schemas.question_pack import QuestionPack_schema
from utills import clean_dict
router = APIRouter(prefix="/questionpack", tags=["Question Pack"])


@router.post("/")
def create_question_pack(questionPack: QuestionPack):
    # db.insert({"title": questionPack.title, "text": questionPack.text}) or as bellow to convert it to Dictionary
    db.insert(questionPack.dict())
    return True

# get a specific questionpack with a specific ID


@router.get("/{id}")
def get_question_pack(id: str):
    pack = db.get(key=id)
    return pack

# retreving all data


@router.get("/")
def get_all_question_pack():
    res = db.fetch()
    return res.items


# update a Question Pack
@router.put("/{key}")
def update_question_pack(update: QuestionPack_schema, key: str,):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=key)
    return True


# Delete a question Pack
@router.delete("/{id}")
def delete_question_pack(id: str):
    db.delete(key=id)
    return True
