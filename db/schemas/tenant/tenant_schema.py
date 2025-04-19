from sqlalchemy import Column, Integer, String, Boolean

from db.schemas.base.base import basemodel


class Tenant(basemodel):
	__tablename__ = "tenants"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String, nullable=False)
	id_document = Column(String, unique=True, index=True, nullable=False)
	email = Column(String, unique=True, index=True, nullable=False)
	phone = Column(String, nullable=True)
	emergency_contact = Column(String(100))
	status = Column(Boolean, nullable=False, default=True)
