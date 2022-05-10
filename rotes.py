from fastapi import APIRouter
from quiz import quiz

routes = APIRouter()

routes.include_router(quiz.router, prefix='/quiz')
