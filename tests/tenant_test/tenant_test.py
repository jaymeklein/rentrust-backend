from datetime import datetime

import pytest
from faker import Faker

from pydantic import ValidationError

from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant_schema import TenantSchema
from db.schemas.tenant.tenant_schema import Tenant as DBTenant
from tests.config import db_session, build_valid_tenant_data, build_invalid_tenant_data, remove_id

TENANT_MODEL = TenantModel(testing=True)
fake = Faker()

def test_create_tenant_schema():
	"""Tests the tenant schema creation

	*Pydantic auto validates column types
	"""
	tenant_data = build_valid_tenant_data()
	tenant_schema = TenantSchema(**tenant_data)
	assert tenant_schema.model_dump() == tenant_data

def test_create_tenant_database_model():
	"""Tests the tenant model creation"""
	tenant_data = build_valid_tenant_data()
	tenant_database_model = DBTenant(**tenant_data)
	assert tenant_database_model.as_dict() == tenant_data

def test_insert_tenant():
	"""Tests if the data inserted is equal to the data sent to be inserted"""
	tenant_data = build_valid_tenant_data()
	tenant_schema = TenantSchema(**tenant_data)
	inserted_tenant = TENANT_MODEL.create_tenant(tenant_schema)
	inserted_tenant = remove_id(inserted_tenant.as_dict())
	tenant_data = remove_id(tenant_data)
	assert inserted_tenant == tenant_data, "Inserted tenant and tenant data should be equal."

def test_insert_tenant_persistence():
	"""Tests if the inserted tenant is persisted in the DB"""
	tenant_data = build_valid_tenant_data()
	tenant_schema = TenantSchema(**tenant_data)
	tenant_schema.email = 'email@tenant.com'
	tenant_schema.id_document = str(datetime.now())
	inserted_tenant = TENANT_MODEL.create_tenant(tenant_schema)
	persisted_tenant = TENANT_MODEL.get_tenant(tenant_id=inserted_tenant.id)

	assert persisted_tenant is not None, "Persisted tenant should not be None."
	assert inserted_tenant.id == persisted_tenant.id, "Inserted tenant ID and persisted tenant ID should be equal."


def test_invalid_email():
	invalid_data = build_valid_tenant_data()
	invalid_mail = "invalid-email@@gmail.com"
	invalid_data['email'] = invalid_mail

	with pytest.raises(ValidationError) as excinfo:
		TenantSchema(**invalid_data)

	assert 'value is not a valid email address' in str(excinfo.value), f"{invalid_mail} should not be considered valid."

def test_empty_email():
	invalid_data = build_invalid_tenant_data()
	invalid_data['email'] = ''

	with pytest.raises(ValidationError) as excinfo:
		TenantSchema(**invalid_data)

	assert 'value is not a valid email address' in str(excinfo.value)

def test_empty_name():
	invalid_data = build_invalid_tenant_data()
	invalid_data['name'] = ''

	with pytest.raises(ValidationError) as excinfo:
		TenantSchema(**invalid_data)

	assert "at least 5 characters [type=string_too_short, input_value=''" in str(excinfo.value)



def test_get_all_tenants():
	TENANT_MODEL.truncate_tenants()

	tenants = [build_valid_tenant_data(random=True) for _ in range(5)]
	tenants = [TenantSchema(**tenant) for tenant in tenants]
	created_tenants = []

	for tenant in tenants:
		created_tenant = TENANT_MODEL.create_tenant(tenant)
		created_tenants.append(created_tenant)

	all_active_tenants = TENANT_MODEL.get_all_tenants()
	all_tenants = TENANT_MODEL.get_all_tenants(get_inactive=True)
	all_active = all(set(tenant.status for tenant in all_active_tenants))

	assert all_active, "Should only query for active tenants."
	assert len(all_tenants) == len(tenants), "Length of inserted tenants should be equal to queried tenants."


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
