from pydantic import BaseModel


class Action(BaseModel):
    action_name: str