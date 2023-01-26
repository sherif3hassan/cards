from typing import Optional

from pydantic import BaseModel


class Answer_schema(BaseModel):
    text: Optional[str]
