from fastapi import FastAPI
from deta import Deta

from models.question import Question

app = FastAPI()

deta = Deta("a0t0pjsh_PrZdmxu7pwZHGJPuGsjw6JhpbbF9Ggfh")

db = deta.Base("/question")


@app.get("/question")
def get_all_questions():
    return db.fetch().items


@app.get("/question/{key}")
def get_question(key: str):
    return db.get(key)


@app.post("/question")
def create_question(question: Question):
    res = db.insert(question.dict())
    return res


@app.put("/question/{key}")
def update_question(key: str, question: dict):
    db.put(question, key)
    return db.get(key)


@app.delete("/question/{key}")
def delete_question(key: str):
    deleted = db.get(key)
    db.delete(key)
    return deleted
