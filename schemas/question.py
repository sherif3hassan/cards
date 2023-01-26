from typing import Optional
from pydantic import BaseModel

class Question_schema(BaseModel):
    text: Optional[str]