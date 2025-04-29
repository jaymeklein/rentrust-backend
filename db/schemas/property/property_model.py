from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Boolean
from db.schemas.base.base import basemodel


class Property(basemodel):
    __tablename__ = "properties"

    # IDs
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True)
    # owner_id = Column(Integer, ForeignKey("owners.id"), index=True, nullable=False)
    # address_id = Column(Integer, ForeignKey("property_addresses.id"))
    # real_estate_company_id = Column(
    # 	Integer, ForeignKey("real_estate_companies.id"), nullable=False
    # )

    # Main columns
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    size_m2 = Column(Float, nullable=False)
    listed_date = Column(DateTime, default=datetime.now())
    last_updated = Column(DateTime, onupdate=datetime.now())
    year_built = Column(Integer)
    is_active = Column(Boolean, default=True)
