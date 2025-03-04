from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.models.base.base import Base
from api.utils.property_enums import PropertyStatuses, PropertyTypes


class Property(Base):
  __tablename__ = "properties"

  # IDs
  id = Column(Integer, primary_key=True, index=True)
  tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True)
  owner_id = Column(Integer, ForeignKey("owners.id"), index=True, nullable=False)
  address_id = Column(Integer, ForeignKey("property_addresses.id"))
  real_state_company_id = Column(Integer, ForeignKey("real_estate_companies.id"), nullable=False)

  # Enum columns
  type = Column(Enum(PropertyTypes), nullable=False, index=True)
  status = Column(Enum(PropertyStatuses), nullable=False, index=True)

  # Main columns
  name = Column(String, nullable=False)  # e.g. "Sunny Villa"
  description = Column(String, nullable=False)
  value = Column(Float, nullable=False)  # Rent value or property value
  size_m2 = Column(Float, nullable=False)  # In M2
  listed_date = Column(DateTime, default=datetime.now())
  last_updated = Column(DateTime, onupdate=datetime.now())
  year_built = Column(Integer)

  # Relationships
  tenant = relationship("Tenant", back_populates="properties")
  owner = relationship("Owner", back_populates="properties")
  address = relationship("property_addresses", back_populates="properties")
  features = relationship("Feature", secondary="real_estate_companies", back_populates="properties")
  managing_company = relationship("real_estate_companies", back_populates="managed_properties")
