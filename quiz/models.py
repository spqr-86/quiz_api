from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class Question(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    answer = Column(String)
    question = Column(String)
    created_at = Column(DateTime)
