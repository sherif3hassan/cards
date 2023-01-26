from typing import List, Optional
from pydantic import BaseModel

class AnswerPack_schema(BaseModel):
    title: Optional[str]
    texts: Optional[List[str]]