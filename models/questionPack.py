from typing import List

from pydantic import BaseModel


class QuestionPack(BaseModel):
    title: str
    text: List[str]  # IDs of Questions
