from fastapi import FastAPI
from deta import Deta
from models.answers import *
from utills import *
app = FastAPI()
deta = Deta("a0t0pjsh_PrZdmxu7pwZHGJPuGsjw6JhpbbF9Ggfh")
db = deta.Base("answer_db")


@app.post("/answers")
async def create_answer(answer: Answer):
    db.insert(answer.dict())
    return answer


@app.get("/answers/{id}")
async def get_answer(id: str):
    return db.get(key=id)


@app.get("/answers/")
async def get_all_answer():
    return db.fetch().items


@app.put("/answers/")
async def update_answer(update: Answer_update, id: str):
    update_dict = clean_dict(update.dict())
    db.update(updates=update_dict, key=id)
    return True


@app.delete("/answers/{id}")
async def delete_answer(id: str):
    db.delete(key=id)
    return True
