from pydantic import BaseModel
from datetime import datetime


class QuestionBase(BaseModel):
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True


class QuestionCreate(QuestionBase):
    pass


class QuestionList(QuestionBase):
    id: int
