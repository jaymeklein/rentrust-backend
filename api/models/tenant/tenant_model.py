from __future__ import annotations

from sqlalchemy import Column, Integer, String

from api.models.base.base import Base


class Tenant(Base):
  __tablename__ = "tenants"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True, index=True, nullable=False)
  phone = Column(String, nullable=True)
  emergency_contact = Column(String(100))
