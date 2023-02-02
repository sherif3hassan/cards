from typing import List
from actions.action import Action

class PickAnswer(Action):
    action_name = "pick_answer"

    # Customized answers for this specific WebSocket
    answers: List[str]