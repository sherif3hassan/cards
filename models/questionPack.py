from pydantic import BaseModel
from typing import List


class QuestionPack(BaseModel):
    title: str
    text : List[str]
    






