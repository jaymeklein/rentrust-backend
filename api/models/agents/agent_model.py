from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.models.base.base import Base


class Agent(Base):
  __tablename__ = "agents"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  email = Column(String(100), unique=True, index=True)
  phone = Column(String(20))
  license_number = Column(String(50))  # Professional license
  company_id = Column(Integer, ForeignKey('real_estate_companies.id'), nullable=False)

  # Relationships
  company = relationship("RealEstateCompany", back_populates="agents")
  listed_properties = relationship("Property", back_populates="listing_agent")
