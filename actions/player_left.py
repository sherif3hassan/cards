from typing import List
from actions.action import Action


class PlayerLeft(Action):
    action_name = "player_left"

    players: List[str]
    player: str