from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.schemas.base.base import basemodel


class DBPropertyFeature(basemodel):
    __tablename__ = "property_features"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    feature_id = Column(Integer, ForeignKey("features.id"))

    properties = relationship(
        "Feature", secondary="Property", back_populates="property_features"
    )
    features = relationship(
        "Property", secondary="Feature", back_populates="property_features"
    )
