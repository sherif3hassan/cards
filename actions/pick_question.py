from typing import List
from actions.action import Action


class PickQuestion(Action):
    action_name = "pick_question"
    questions: List[str]