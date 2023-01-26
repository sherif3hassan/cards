from deta import Deta  # Import Deta
from fastapi import FastAPI

from models.answerpack import *

app = FastAPI()


# Initialize with a Project Key
deta = Deta("a0t0pjsh_PrZdmxu7pwZHGJPuGsjw6JhpbbF9Ggfh")

# This how to connect to or create a database.
db = deta.Base("answer_packs_db")


@app.post("/create_answerpack/")
def create_answerpack(answer_pack: AnswerPack):

    db.insert(answer_pack.dict())
    return True


@app.get("/answerpacks/{id}")
def get_answer(id: str):
    return db.get(key=id)


@app.get("/answerpacks")
def get_all_answer_packs():
    res = db.fetch()
    return res.items


@app.put("/update_answerpack/{id}")
def update_answer_pack(update: dict, id: str):

    if len(update.keys()) > 2:
        return False

    for key in update.keys():
        if key != "title" and key != "texts":
            return False

    db.update(updates=update, key=id)
    return True


@app.delete("/delete_answerpack")
def delete_answer_pack(id: str):
    db.delete(key=id)
    return True
