import pytest
from pydantic import ValidationError
from sqlalchemy.orm import Session

from api.schemas.tenant_schema import TenantSchema
from db.schemas.tenant.tenant_schema import Tenant as DBTenant
from tests.config import db_session


def build_tenant_data():
	# noinspection PyTypeChecker
	return dict({
		"name"             : "Dummy Tenant",
		"id_document"      : "dummy_id_document_123",
		"email"            : "dummy_tenant_email@tenant.com",
		"phone"            : "+00 (00) 0000-0000",
		"emergency_contact": "+11 (11) 1111-1111",
		"status"           : True
	})


def test_create_tenant_successful(db_session: Session):
	"""Tests pydantic typing, SQLAlchemy model creation, database insertion and persistence"""

	def test_create_tenant_schema(tenant: dict):
		# Any malformed data will be handled by pydantic
		return TenantSchema(**tenant)

	def test_create_tenant_db_model(schema: TenantSchema):
		return DBTenant(**schema.model_dump())

	def test_insert_tenant(model: DBTenant):
		db_session.add(model)
		db_session.commit()
		db_session.flush()
		return model

	def test_tenant_persistence(model: DBTenant):
		found_tenant = (
			db_session
			.query(DBTenant)
			.filter(DBTenant.id == model.id)
			.first()
		)

		assert found_tenant == model

	tenant_data = build_tenant_data()
	tenant_schema = test_create_tenant_schema(tenant_data)
	tenant_model = test_create_tenant_db_model(tenant_schema)
	db_tenant = test_insert_tenant(tenant_model)
	test_tenant_persistence(db_tenant)


def test_create_tenant_error():
	def test_invalid_email():
		invalid_data = build_tenant_data()
		invalid_data['email'] = "invalid-email@@gmail.com"

		with pytest.raises(ValidationError) as excinfo:
			TenantSchema(**invalid_data)

		assert 'value is not a valid email address' in str(excinfo.value)

	def test_empty_email():
		invalid_data = build_tenant_data()
		invalid_data['email'] = ''

		with pytest.raises(ValidationError) as excinfo:
			TenantSchema(**invalid_data)

		assert 'value is not a valid email address' in str(excinfo.value)

	def test_empty_name():
		invalid_data = build_tenant_data()
		invalid_data['name'] = ''

		with pytest.raises(ValidationError) as excinfo:
			TenantSchema(**invalid_data)

		assert "at least 5 characters [type=string_too_short, input_value=''" in str(excinfo.value)

	test_invalid_email()
	test_empty_email()
	test_empty_name()


def test_get_all_tenants():
	"""Not yet implemented"""
	pass


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
