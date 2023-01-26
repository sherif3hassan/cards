from typing import List

from pydantic import BaseModel


class AnswerPack(BaseModel):
    title: str
    texts: List[str]
