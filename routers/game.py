from fastapi import APIRouter, Depends
from database import get_answerpack_db, get_questionpack_db, get_your_game_on
from models.game import Game
from schemas.game import GameSchema

router = APIRouter(prefix='/game', tags=["Game"])


@router.post("/")
def create_new_game(game: GameSchema, 
Question_pack_db=Depends(get_questionpack_db), 
Answer_pack_db=Depends(get_answerpack_db) , 
                    Game_db=Depends(get_your_game_on)):
    new_game = Game(game.mode, rounds= game.rounds , number_of_players=game.max_players,  round_time= game.round_time , questions= game.question_packs_ids , answers=game.answer_packs_ids)             
    Obj = Game_db.insert(new_game.dict())  

    Obj['key']
#    Obj.get('key')
    return Obj['key']
    
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

