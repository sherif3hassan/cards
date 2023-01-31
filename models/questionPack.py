from typing import List

from pydantic import BaseModel


class QuestionPack(BaseModel):
    title: str
    texts: List[str]
