from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.scoping import scoped_session

DATABASE_URL = "sqlite:///base.db"

engine = create_engine(
  DATABASE_URL, echo=True
)  # `echo=True` only for debugging purposes, remove in production.

session_factory = sessionmaker(bind=engine)
instantiated_session = scoped_session(session_factory)


def get_session() -> Session:
  return instantiated_session()
