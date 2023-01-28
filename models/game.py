from typing import List
from pydantic import BaseModel
from enum import Enum
from common.game import GameMode

class GameState(str, Enum):
    waiting = "waiting" # Waiting for players to join the game
    czar_picking = "czar_picking"
    round_running = "round_running" # Players picking answers
    round_ended = "round_ended" # Czar picking winning answer

class PlayedCard(BaseModel):
    player: str    # by ID
    card: str      # by ID
    # Named card since the game mode can be "normal" or "reverse"
    # Look GameState


class Game(BaseModel):
    # Input by user
    mode: GameMode
    rounds: int
    number_of_players: int
    round_time: int
    questions: List[str]
    answers: List[str]

    host: str
    players: List[str]

    current_round: int = 0
    chosen_question: str | None = None
    turn: str = 0
    game_state: GameState = GameState.waiting
    played: List[PlayedCard] = [] # Gets cleared every round