from typing import Optional
from pydantic import BaseModel


class Answer(BaseModel):
    text: str


class Answer_update(BaseModel):
    text: Optional[str]