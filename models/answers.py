from typing import Optional
from pydantic import BaseModel


class Answer(BaseModel):
    text: str
    monkey: str


class Answer_update(BaseModel):
    text: Optional[str]
    monkey: Optional[str]
