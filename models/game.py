from enum import Enum
from typing import List, Union

from pydantic import BaseModel

from common.game import GameMode


class GameState(str, Enum):
    waiting = "waiting"  # Waiting for players to join the game
    czar_picking = "czar_picking"
    round_running = "round_running"  # Players picking answers
    round_ended = "round_ended"  # Czar picking winning answer


class PlayedCard(BaseModel):
    player: str  # by ID
    card: str  # by ID
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

    host: Union[str, None] = None
    players: List[str] = []

    current_round: int = 0
    chosen_question: Union[str, None]
    turn: str = 0
    game_state: GameState = GameState.waiting
    played: List[PlayedCard] = []  # Gets cleared every round
