from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.models.base.base import Base


class Owner(Base):
  __tablename__ = "owners"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  email = Column(String(100), unique=True, index=True)
  phone = Column(String(20))

  # Relationships
  properties = relationship("Property", back_populates="owner")
  company_id = Column(Integer, ForeignKey("real_estate_companies.id"), nullable=True)
  managing_company = relationship("RealEstateCompany", back_populates="owners")
