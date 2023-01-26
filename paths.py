from typing import Union
from deta import Deta
from fastapi import FastAPI
from models.questionPack import QuestionPack



app = FastAPI()


#Intialize with a project Key
deta = Deta("a0t0pjsh_PrZdmxu7pwZHGJPuGsjw6JhpbbF9Ggfh")

#create DATA BASE
db = deta.Base("QuestionPack")
 

@app.post("/questionPack")
def create_question_pack(questionPack: QuestionPack):
    #db.insert({"title": questionPack.title, "text": questionPack.text}) or as bellow to convert it to Dictionary
    db.insert(questionPack.dict())
    return True

#get a specific questionpack with a specific ID 
@app.get("/questionPack/{id}")
def get_question_pack(id: str):
    pack = db.get(key=id)
    return pack

#retreving all data
@app.get("/questionPackAll")
def get_all_question_pack():
    res = db.fetch()
    return res.items

    
#update a Question Pack 
@app.put("/questionPack/{id}")
def update_question_pack(id: str, update: dict):

    if len(update.keys()) > 2:
        return False

    for key in update.keys():
        if key != "title" and key != "text":
            return False


    db.update(key=id , updates=update)
    return True


#Delete a question Pack
@app.delete("/questionPack/{id}")
def delete_question_pack(id:str):
    db.delete(key=id)
    return True



