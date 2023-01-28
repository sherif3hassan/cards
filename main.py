from fastapi import FastAPI

from routers.answer import router as answer_router
from routers.answer_pack import router as answer_pack_router
from routers.question import router as question_router
from routers.question_pack import router as question_pack_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(question_router)
app.include_router(answer_router)
app.include_router(question_pack_router)
app.include_router(answer_pack_router)
