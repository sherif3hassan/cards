from fastapi import FastAPI
from question import router as question_router

app = FastAPI()

app.include_router(question_router)