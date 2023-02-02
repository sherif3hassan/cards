from typing import List
from actions.action import Action


class NewPlayerJoined(Action):
    action_name = "new_player_joined"
    players: List[str]
    new_player: str