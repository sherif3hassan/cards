from typing import List
from actions.action import Action


class CzarChoseQuestion(Action):
    action_name = "czar_chose_question"
    answers: List[str]