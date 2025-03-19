import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine

load_dotenv('.env')

DATABASE_URL = os.environ.get("PRIVATE_DATABASE_URL")
PRODUCTION = os.environ.get("PRIVATE_PRODUCTION", False) == 'true'


def generate_engine(url: str, echo: bool) -> Engine:
	return create_engine(url, echo=echo)


def get_engine() -> Engine:
	return generate_engine(DATABASE_URL, PRODUCTION)
