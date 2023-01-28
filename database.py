from decouple import config
from deta import Deta

OUR_DETA_PROJECT_KEY = config("OUR_DETA_PROJECT_KEY")

deta = Deta(OUR_DETA_PROJECT_KEY)


def get_your_game_on():
    return deta.Base("game")

def get_answer_db():
    return deta.Base("answer")


def get_questionpack_db():
    return deta.Base("questionpack")


def get_answerpack_db():
    return deta.Base("answerpack")


def get_question_db():
    return deta.Base("question")