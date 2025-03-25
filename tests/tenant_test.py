from sqlalchemy.orm import Session

from db.schemas.tenant.tenant_schema import Tenant as DBTenant
from tests.config import db_session


def test_get_all_tenants():
	"""Not yet implemented"""
	pass


def test_create_tenant(db_session: Session):
	"""Tests pydantic typing, SQLAlchemy model creation and database insertion"""

	def build_tenant_data():
		# noinspection PyTypeChecker
		return {
			"name"             : "Dummy Tenant",
			"id_document"      : "dummy_id_document_123",
			"email"            : "dummy_tenant_email@tenant.com",
			"phone"            : "+00 (00) 0000-0000",
			"emergency_contact": "+11 (11) 1111-1111",
			"status"           : True
		}

	def test_create_tenant_db_model(tenant_data: dict):
		return DBTenant(**tenant_data)

	def test_insert_tenant(tenant_model: DBTenant):
		db_session.add(tenant_model)
		db_session.flush()
		db_session.commit()
		return tenant_model

	def test_tenant_persistance(tenant_model: DBTenant):
		found_tenant = (
			db_session
			.query(DBTenant)
			.filter(DBTenant.id == tenant_model.id)
			.first()
		)

		assert found_tenant == tenant_model

	tenant_data = build_tenant_data()
	tenant_model = test_create_tenant_db_model(tenant_data)
	test_insert_tenant(tenant_model)

	selected_tenant = test_tenant_persistance(tenant_model)


def test_get_tenant():
	"""Not yet implemented"""
	pass


def test_update_tenant():
	"""Not yet implemented"""
	pass


def test_delete_tenant():
	"""Not yet implemented"""
	pass


def test_tenant_exists():
	"""Not yet implemented"""
	pass
