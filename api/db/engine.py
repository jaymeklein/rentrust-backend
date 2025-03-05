from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL = "sqlite:///base.db"

engine = create_engine(
    DATABASE_URL, echo=True
)  # `echo=True` only for debugging purposes, remove in production.


def get_engine() -> Session:
    return engine


if __name__ == '__main__':
    engine = get_engine()
    pass