import json
import requests

from .models import Question
from .schemas import QuestionCreate


service_url = 'https://jservice.io/api/random/'


def get_all_questions(db):
    return db.session.query(Question).all()


def get_questions_from_api(url: str, count: int):
    parameters = {
        'count': count,
    }
    try:
        response = requests.get(url, params=parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return '<ошибка на сервере>'


def check_exist(db, question):
    q = db.session.query(Question).filter(
        Question.question == question['question'],
        Question.answer == question['answer'],
    )
    return db.session.query(q.exists()).scalar()


def create_questions(db, count: int):
    questions = get_questions_from_api(service_url, count)

    for q in questions:
        if db.session.query(Question):
            while check_exist(db, q):
                q = get_questions_from_api(service_url, 1)

        question = QuestionCreate(**q)
        db_question = Question(
            question=question.question,
            answer=question.answer,
            created_at=question.created_at,
        )
        db.session.add(db_question)
        db.session.commit()
        db.session.refresh(db_question)
