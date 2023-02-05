from typing import List

from pydantic import BaseModel

from common.game import GameMode


class GameSchema(BaseModel):
    mode: GameMode
    rounds: int
    max_players: int
    round_time: int
    all_packs: bool
    question_packs_ids: List[str]
    answer_packs_ids: List[str]
