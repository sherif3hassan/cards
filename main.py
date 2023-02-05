from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.answer_pack import router as answer_pack_router
from routers.auth import router as auth_router
from routers.question_pack import router as question_pack_router
from routers.game import router as game_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(game_router)
app.include_router(question_pack_router)
app.include_router(answer_pack_router)
