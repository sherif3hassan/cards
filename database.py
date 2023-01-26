from decouple import config
from deta import Deta


OUR_DETA_PROJECT_KEY = config("OUR_DETA_PROJECT_KEY")

deta = Deta(OUR_DETA_PROJECT_KEY)

answer_db = deta.Base("answer")
questionpack_db = deta.Base("questionpack")
answerpack_db = deta.Base("answerpack")

def get_question_db():
    return deta.Base("question")