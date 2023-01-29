from fastapi import APIRouter, Depends

from common.utills import clean_dict
from database import get_answer_db
from models.answer import Answer
from schemas.answer import Answer_schema

router = APIRouter(prefix="/answer", tags=["Answer"])


@router.post("/")
async def create_answer(answer: Answer, db=Depends(get_answer_db)):
    db.insert(answer.dict())
    return answer


@router.get("/{id}")
async def get_answer(id: str, db=Depends(get_answer_db)):
    return db.get(key=id)


@router.get("/")
async def get_all_answer(db=Depends(get_answer_db)):
    return db.fetch().items


@router.put("/{key}")
async def update_answer(update: Answer_schema, key: str, db=Depends(get_answer_db)):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=key)
    db
    return True


@router.delete("/{id}")
async def delete_answer(id: str, db=Depends(get_answer_db)):
    db.delete(key=id)
    return True
