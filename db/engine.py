from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv('.env')

DATABASE_URL = "sqlite:///base.db"

engine = create_engine(
	DATABASE_URL, echo=os.environ.get("PRODUCTION", False) == 'true'
)


def get_engine() -> Engine:
	return engine
