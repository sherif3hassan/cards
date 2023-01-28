from fastapi import APIRouter, Depends
from schemas.game import GameSchema

router = APIRouter(prefix='/game', tags=["Game"])


@router.post("/")
def create_new_game(game: GameSchema):
    # Return room ID
    ...


@router.get("/{room_id}/someonejoined")
def respond_when_someone_joins():
    # Monitors two thing in the database
    # Responds to the client when a new player is added in the Game[room_id]
    # Returns the new player
    pass


@router.get("/{room_id}/waitingforgametostart")
def respond_when_game_starts():
    # Monitor database for the condition:  len(players) == number_of_players
    # Responds when the Game[room_id]'s state becomes RoundRunning
    # Returned value depends on the requesting user
        # If host (i.e. Card czar)
    # Returns question cards
        # Else
    # Returns answer cards
    pass


@router.post("/{room_id}/join")
def join_game(room_id: str):
    # check how many players are in Game[room_id]
    # DOESNOT add player if len(players) == number_of_players
    ...


@router.post("/{room_id}/waitingforczarpick")
def responed_when_czar_picks(room_id: str):
    pass


@router.post("/{room_id}/pickaquestion")
def pick_a_question(room_id: str):
    pass


@router.post("/{room_id}/pickananswer")
def pick_an_answer(room_id: str):
    pass

