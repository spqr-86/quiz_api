from fastapi import APIRouter, Query
from fastapi_sqlalchemy import db

from . import servise, models


router = APIRouter()


@router.get("/questions/")
def get_all_questions():
    db_questions = servise.get_all_questions(db)
    return db_questions


@router.post("/questions/")
def create_questions(count: int = Query(..., gt=0)):
    servise.create_questions(db, count)
    return db.session.query(models.Question).order_by(models.Question.id.desc()).first()
