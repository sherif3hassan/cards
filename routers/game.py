from typing import Dict, List

from pydantic import BaseModel
from actions.new_player_joined import NewPlayerJoined
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from actions.player_left import PlayerLeft
from routers.auth import TokenData, get_token_data


router = APIRouter(prefix="/game")


class Player:
    def __init__(self, username: str, ws: WebSocket):
        self.username = username
        self.websocket = ws


class GameSettings(BaseModel):
    mode: int
    max_players: int
    number_of_rounds: int
    round_time: int


class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.settings: GameSettings = GameSettings(
            max_players=10,
            mode=1,
            number_of_rounds=5,
            round_time=60
        )

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def is_empty(self) -> bool:
        return len(self.players) == 0


class GameManager:
    def __init__(self):
        # Game = { room_id: list of connected users }
        self.games: Dict[str, Game] = dict()

    async def connect(self, room_id: str, player: Player):
        # Add a new connection to this room
        await player.websocket.accept()

        # If game with ID `room_id` does not exist
        if self.games.get(room_id, None) is None:
            self.games[room_id] = Game()
            self.games[room_id].add_player(player)

            await player.websocket.send_json({"message": "Game created with default settings"})
            # Create an empty game with ID `room_id`
            # player is the Host
            # Receive game settings from the Host
            game_settings: dict = await player.websocket.receive_json()
            
            self.games[room_id].settings = GameSettings(
                max_players=game_settings["max_players"],
                number_of_rounds=game_settings["number_of_rounds"],
                round_time=game_settings["round_time"],
                mode=game_settings["mode"]
            )
            
            await self.broadcast(room_id=room_id, message={
                "message": "Game settings updated"
            }, sender=None)
        else:
            self.games[room_id].add_player(player)

            await self.broadcast(room_id,
                                NewPlayerJoined(
                                    players=[
                                        p.username for p in self.games[room_id].players],
                                    new_player=player.username
                                ).dict(),
                                player)

    async def disconnect(self, room_id: str, player: Player):
        # Remove the connection from the room
        self.games[room_id].remove_player(player)

        await self.broadcast(room_id,
                             PlayerLeft(
                                 players=[
                                     p.username for p in self.games[room_id].players],
                                 player=player.username
                             ).dict(),
                             player)

        # If the game has no players
        if self.games[room_id].is_empty():
            # Delete the game
            del self.games[room_id]

    async def broadcast(self, room_id: str, message: dict, sender: Player):
        if self.games.get(room_id, None) is None:
            return

        for player in self.games[room_id].players:
            if player is not sender:
                await player.websocket.send_json(message)


manager = GameManager()


@router.put("/{room_id}")
def update_game(room_id: str, game_updates: GameSettings):
    manager.games[room_id].settings = game_updates
    return True


@router.websocket("/play")
async def play(
    websocket: WebSocket,
    token_data: TokenData = Depends(get_token_data)
):
    username = token_data.username
    room_id = token_data.room_id

    player = Player(username, websocket)
    await manager.connect(room_id=room_id, player=player)

    try:
        while True:
            message = await websocket.receive_json()
            print(username, "said", message)
    except WebSocketDisconnect:
        await manager.disconnect(room_id=room_id, player=player)
