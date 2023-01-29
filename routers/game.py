from database import get_answerpack_db, get_questionpack_db, get_your_game_on
from models.game import Game
from common.utills import TokenData, get_token_data
from fastapi import APIRouter, Depends, HTTPException
from database import get_your_game_on
from schemas.game import GameSchema
from deta.base import _Base

router = APIRouter(prefix="/game", tags=["Game"])


@router.post("/")
def create_new_game(
    game: GameSchema,
    questionpack_db=Depends(get_questionpack_db),
    answerpack_db=Depends(get_answerpack_db),
    game_db=Depends(get_your_game_on)
):
    new_game = Game(
        mode=game.mode,
        rounds=game.rounds,
        number_of_players=game.max_players,
        round_time=game.round_time,
        questions=game.question_packs_ids,
        answers=game.answer_packs_ids
    )

    game_in_db = game_db.insert(new_game.dict())

    return game_in_db['key']


@router.get("/monitor_players")
def respond_when_players_change(token_data: TokenData = Depends(get_token_data), game_db: _Base = Depends(get_your_game_on)):
    # Monitors two thing in the database
    # Responds to the client when a new player is added in the Game[room_id]
    # Returns the new player

    # Store the CURRENT size of players
    # As long as the CURRENT size is the same as the actual size of players in the database
    # do nothing
    # else, return the new list of players

    game = game_db.get(key=token_data.room_id)
    current_number_of_players = len(game["players"])

    while current_number_of_players == len(game_db.get(key=token_data.room_id)["players"]):
        pass

    updated_list_of_players = game_db.get(key=token_data.room_id)["players"]

    return updated_list_of_players


@router.get("/monitor_game_start")
def respond_when_game_starts(token_data: TokenData = Depends(get_token_data), game_db=Depends(get_your_game_on)):
    number_of_players = game_db.get(key=token_data.room_id)["number_of_players"]

    while len(game_db.get(key=token_data.room_id)["players"]) != number_of_players:
        pass

    # Monitor database for the condition:  len(players) == number_of_players
    # Responds when the Game[room_id]'s state becomes RoundRunning
    # Returned value depends on the requesting user
    # If host (i.e. Card czar)
    # Returns question cards
    # Else
    # Returns answer cards


@router.post("/join")
def join_game(game_db: _Base = Depends(get_your_game_on), token_data: TokenData = Depends(get_token_data)):
    # check how many players are in Game[room_id]
    # DOESNOT add player if len(players) == number_of_players
    game = game_db.get(key=token_data.room_id)
    if game["number_of_players"] == len(game["players"]):
        raise HTTPException(status_code=404, detail="room is full")
    players = game["players"]
    players.append(token_data["username"])
    game["players"] = players
    game_db.update(updates=game)
    return True


@router.post("/{room_id}/waitingforczarpick")
def responed_when_czar_picks(room_id: str):
    pass


@router.post("/{room_id}/pickaquestion")
def pick_a_question(room_id: str, db=Depends(get_your_game_on)):
    pass


@router.post("/{room_id}/pickananswer")
def pick_an_answer(room_id: str):
    pass
