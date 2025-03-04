from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.models.agents.agent_model import Agent
from api.models.base.base import Base
from api.models.property.property_model import Property


class RealEstateCompany(Base):
  __tablename__ = "real_estate_companies"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False, unique=True)
  email = Column(String(100), unique=True, index=True)
  phone = Column(String(20))
  website = Column(String(100))
  registration_number = Column(String(50), unique=True)  # Business license ID

  # Relationships
  agents = relationship(Agent, back_populates="company")  # Company employees
  managed_properties = relationship(Property, back_populates="managing_company")
