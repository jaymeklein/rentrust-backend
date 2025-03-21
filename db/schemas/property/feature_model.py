

from sqlalchemy import Column, Integer, String

from db.schemas.base.base import Base


class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False, default=1)
