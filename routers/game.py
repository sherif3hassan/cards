from typing import Dict, List
from actions.new_player_joined import NewPlayerJoined
from database import get_answerpack_db, get_questionpack_db, get_your_game_on
from models.game import Game
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from database import get_your_game_on
from routers.auth import TokenData, get_token_data
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
    questions = []
    answers = []

    for qpid in game.question_packs_ids:
        x = questionpack_db.get(qpid)
        questions.extend(x["texts"])

    for apid in game.answer_packs_ids:
        x = answerpack_db.get(apid)
        answers.extend(x["texts"])

    new_game = Game(
        mode=game.mode,
        rounds=game.rounds,
        number_of_players=game.max_players,
        round_time=game.round_time,
        questions=questions,
        answers=answers
    )

    game_in_db = game_db.insert(new_game.dict())

    return game_in_db['key']


# @router.post("/monitor_players")
# def respond_when_players_change(body: dict, token_data: TokenData = Depends(get_token_data), game_db: _Base = Depends(get_your_game_on)):
#     # Monitors two thing in the database
#     # Responds to the client when a new player is added in the Game[room_id]
#     # Returns the new player

#     # Store the CURRENT size of players
#     # As long as the CURRENT size is the same as the actual size of players in the database
#     # do nothing
#     # else, return the new list of players

#     number_of_players = body["number_of_players"]

#     while number_of_players == len(game_db.get(key=token_data.room_id)["players"]):
#         pass

#     updated_list_of_players = game_db.get(key=token_data.room_id)["players"]

#     return updated_list_of_players


# @router.post("/monitor_game_start")
# def respond_when_game_starts(token_data: TokenData = Depends(get_token_data), game_db=Depends(get_your_game_on)):
#     number_of_players = game_db.get(key=token_data.room_id)["number_of_players"]

#     while len(game_db.get(key=token_data.room_id)["players"]) != number_of_players:
#         pass

#     # Monitor database for the condition:  len(players) == number_of_players
#     # Responds when the Game[room_id]'s state becomes RoundRunning
#     # Returned value depends on the requesting user
#     # If host (i.e. Card czar)
#     # Returns question cards
#     # Else
#     # Returns answer card
#     game = game_db.get(key=token_data.room_id)
#     if game["host"] == token_data.username:
#         return game["questions"]
#     else:
#         return game["answers"]


# @router.post("/join")
# def join_game(
#     game_db: _Base = Depends(get_your_game_on),
#     token_data: TokenData = Depends(get_token_data)
# ):
#     # check how many players are in Game[room_id]
#     # DOESNOT add player if len(players) == number_of_players
#     game = game_db.get(key=token_data.room_id)
#     if game["number_of_players"] == len(game["players"]):
#         raise HTTPException(status_code=403, detail="room is full")

#     players = game["players"]
#     players.append(token_data.username)
#     game["players"] = players

#     # Delete the primary key before update
#     # since updating a record's primary key is Forbidden
#     del game["key"]

#     if game["host"] is None:
#         game["host"] = token_data.username

#     game_db.update(updates=game, key=token_data.room_id)

#     return True

class Player:
    def __init__(self, username: str, ws: WebSocket) -> None:
        self.username = username
        self.websocket = ws


class Game:
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.current_round = 0


class ConnectionManager:
    def __init__(self):
        # Game = { room_id: list of connected users }
        self.games: Dict[str, Game] = dict()

    async def connect(self, room_id: str, player: Player):
        # If game with ID `room_id` does not exist
        if self.games.get(room_id, None) is None:
            # Create an empty game with ID `room_id`
            self.games[room_id] = []

        # Add a new connection to this room
        await player.websocket.accept()

        for ws in self.games[room_id]:
            await ws.send_json(
                NewPlayerJoined(
                    players=[p.username for p in self.games[room_id]],
                    new_player=player.username
                ).dict()
            )

        self.games[room_id].append(player.websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        # Remove the connection from the room
        self.games[room_id].remove(websocket)

        # If the game has no players
        if len(self.games[room_id]) == 0:
            # Delete the game
            del self.games[room_id]

    async def broadcast(self, room_id: str, message: str):
        if self.games.get(room_id, None) is None:
            return

        for websocket in self.games[room_id]:
            await websocket.send_text(message)


manager = ConnectionManager()


@router.websocket("/join")
async def join(
    websocket: WebSocket,
    token_data: TokenData = Depends(get_token_data)
):
    room_id = token_data.room_id

    await manager.connect(room_id=room_id, websocket=websocket)
    try:
        while True:
            # Listen for events
                # Another player joined (monitoring players)
                # Game started
            pass
    except WebSocketDisconnect:
        await manager.disconnect(room_id=room_id, websocket=websocket)


@router.post("/{room_id}/waitingforczarpick")
def responed_when_czar_picks(room_id: str):
    pass


@router.post("/{room_id}/pickaquestion")
def pick_a_question(room_id: str, db=Depends(get_your_game_on)):
    pass


@router.post("/{room_id}/pickananswer")
def pick_an_answer(room_id: str):
    pass
