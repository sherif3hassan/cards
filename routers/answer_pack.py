from deta import Deta  # Import Deta
from fastapi import APIRouter
from models.answerpack import *

from constants import OUR_DETA_PROJECT_KEY
deta = Deta(OUR_DETA_PROJECT_KEY)

router = APIRouter(prefix='/answerpack', tags=["Answer Pack"])


# This how to connect to or create a database.
db = deta.Base("answer_packs_db")


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


@router.put("/{id}")
def update_answer_pack(update: dict, id: str):
    if len(update.keys()) > 2:
        return False

    for key in update.keys():
        if key != "title" and key != "texts":
            return False

    db.update(updates=update, key=id)
    return True


@router.delete("/")
def delete_answer_pack(id: str):
    db.delete(key=id)
    return True
