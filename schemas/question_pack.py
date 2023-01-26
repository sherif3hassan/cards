from typing import List, Optional
from pydantic import BaseModel

class QuestionPack_schema(BaseModel):
    title:Optional[str]
    text : Optional[List[str]]
    