from datetime import datetime
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from db.schemas.base.base import basemodel
from api.utils.property_enums import PropertyStatus, PropertyType


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

	# Enum columns
	type = Column(Enum(PropertyType), nullable=False, index=True)
	status = Column(Enum(PropertyStatus), nullable=False, index=True)

	# Main columns
	name = Column(String, nullable=False)  # e.g. "Sunny Villa"
	description = Column(String, nullable=False)
	value = Column(Float, nullable=False)  # Rent value or property value
	size_m2 = Column(Float, nullable=False)  # In M2
	listed_date = Column(DateTime, default=datetime.now())
	last_updated = Column(DateTime, onupdate=datetime.now())
	year_built = Column(Integer)
