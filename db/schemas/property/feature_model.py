from sqlalchemy import Column, Integer, String

from db.schemas.base.base import basemodel


class Feature(basemodel):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False, default=1)
