from decouple import config
from deta import Deta

OUR_DETA_PROJECT_KEY = config("OUR_DETA_PROJECT_KEY")

deta = Deta(OUR_DETA_PROJECT_KEY)

question_db = deta.Base("question")
answer_db = deta.Base("answer")


def get_questionpack_db():
    return deta.Base("questionpack")


def get_answerpack_db():
    return deta.Base("answerpack")
