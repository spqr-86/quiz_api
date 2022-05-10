import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from rotes import routes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(routes)
