from __future__ import annotations
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base(metadata=MetaData())
Base.__table_args__ = {'extend_existing': True}
