from __future__ import annotations

from sqlalchemy import Column, Integer, String

from api.models.base.base import Base


class PropertyAddress(Base):
  __tablename__ = "property_addresses"

  id = Column(Integer, primary_key=True, index=True)

  street_address = Column(String, nullable=False)
  unit = Column(String)  # Or number
  city = Column(String, nullable=False)
  state = Column(String, nullable=False)
  country = Column(String, nullable=False)
  zip_code = Column(String)
  district = Column(String)  # Or neighborhood
