from datetime import datetime

import pytest
from faker import Faker
from pydantic import ValidationError

from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant.tenant_schema import SearchTenantSchema, TenantSchema
from db.schemas.tenant.tenant_schema import Tenant as DBTenant
from tests.config import build_valid_tenant_data, build_invalid_tenant_data, remove_id

TENANT_MODEL = TenantModel(testing=True)
fake = Faker()


@pytest.fixture(autouse=True)
def truncate_tenants():
    TENANT_MODEL.truncate_tenants()


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
    assert inserted_tenant == tenant_data, (
        "Inserted tenant and tenant data should be equal."
    )


def test_insert_tenant_persistence():
    """Tests if the inserted tenant is persisted in the DB"""
    tenant_data = build_valid_tenant_data()
    tenant_schema = TenantSchema(**tenant_data)
    tenant_schema.email = "email@tenant.com"
    tenant_schema.id_document = str(datetime.now())
    inserted_tenant = TENANT_MODEL.create_tenant(tenant_schema)
    persisted_tenant = TENANT_MODEL.get_tenant(tenant_id=inserted_tenant.id)

    assert persisted_tenant is not None, "Persisted tenant should not be None."
    assert inserted_tenant.id == persisted_tenant.id, (
        "Inserted tenant ID and persisted tenant ID should be equal."
    )


def test_invalid_email():
    """Tests for invalid email raise"""
    invalid_data = build_valid_tenant_data()
    invalid_mail = "invalid-email@@gmail.com"
    invalid_data["email"] = invalid_mail

    with pytest.raises(ValidationError) as excinfo:
        TenantSchema(**invalid_data)

    assert "value is not a valid email address" in str(excinfo.value), (
        f"{invalid_mail} should not be considered valid."
    )


def test_empty_email():
    """Tests for empty email raise"""
    invalid_data = build_invalid_tenant_data()
    invalid_data["email"] = ""

    with pytest.raises(ValidationError) as excinfo:
        TenantSchema(**invalid_data)

    assert "value is not a valid email address" in str(excinfo.value)


def test_empty_name():
    """Tests for empty name raise"""
    invalid_data = build_invalid_tenant_data()
    invalid_data["name"] = ""

    with pytest.raises(ValidationError) as excinfo:
        TenantSchema(**invalid_data)

    assert "at least 5 characters [type=string_too_short, input_value=''" in str(
        excinfo.value
    )


def test_get_all_tenants():
    """Tests for getting all tenants"""

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
    assert len(all_tenants) == len(tenants), (
        "Length of inserted tenants should be equal to queried tenants."
    )


def test_update_tenant():
    """Tests for updating a tenant"""

    tenant_data = build_valid_tenant_data()
    tenant_schema = TenantSchema(**tenant_data)
    inserted_tenant = TENANT_MODEL.create_tenant(tenant_schema)

    new_tenant_data = build_valid_tenant_data(random=True)
    new_tenant_schema = TenantSchema(**new_tenant_data)
    updated_tenant = TENANT_MODEL.update_tenant(inserted_tenant.id, new_tenant_schema)

    assert inserted_tenant.id == updated_tenant.id, (
        "Inserted tenant and updated tenant should have the same ID."
    )
    assert inserted_tenant.as_dict() != updated_tenant.as_dict(), (
        "Inserted tenant and updated tenant should not be equal."
    )
    assert set(inserted_tenant.__dict__.keys()) == set(
        updated_tenant.__dict__.keys()
    ), "Inserted tenant and updated tenant should have the same attributes."


def test_delete_tenant():
    """Tests for deleting a tenant"""
    tenant_data = build_valid_tenant_data()
    tenant_schema = TenantSchema(**tenant_data)

    inserted_tenant = TENANT_MODEL.create_tenant(tenant_schema)
    deleted_tenant = TENANT_MODEL.delete_tenant(inserted_tenant)

    assert deleted_tenant.deleted, "Deleted tenant should have deleted status as True."
    assert deleted_tenant.error is None, "Deleted tenant should not have any errors."


def test_tenant_exists():
    """Tests for tenant_exists method"""
    tenant_data = build_valid_tenant_data()
    tenant_schema = TenantSchema(**tenant_data)
    TENANT_MODEL.create_tenant(tenant_schema)

    existing_tenants = TENANT_MODEL.tenant_exists(tenant_schema)
    assert existing_tenants, "Tenant should exist after being inserted."

    invalid_tenant_data = build_valid_tenant_data(random=True)
    invalid_tenant_schema = TenantSchema(**invalid_tenant_data)
    non_existing_tenants = TENANT_MODEL.tenant_exists(invalid_tenant_schema)
    assert not non_existing_tenants, (
        "Tenant should not exist after being inserted with invalid data."
    )


def test_filter_tenants():
    """Tests for filter_tenants method"""
    tenant_data = build_valid_tenant_data(random=True)
    tenant_schema = TenantSchema(**tenant_data)
    tenant_schema.name = "John Doe"
    tenant_schema.email = "john.doe@example.com"
    tenant_schema.phone = "1234567890"

    TENANT_MODEL.create_tenant(tenant_schema)

    second_tenant_data = build_valid_tenant_data(random=True)
    second_tenant_schema = TenantSchema(**second_tenant_data)
    second_tenant_schema.name = "Maria Doe"
    second_tenant_schema.email = "maria.doe@example.com"
    second_tenant_schema.phone = "9876543210"
    TENANT_MODEL.create_tenant(second_tenant_schema)

    filter_tenant_schema = SearchTenantSchema(name="Doe")
    filtered_tenants = TENANT_MODEL.filter_tenants(filter_tenant_schema)
    assert filtered_tenants, "Filtered tenants should exist after being inserted."
    assert len(filtered_tenants) == 2, "Filtered tenants should have two tenants."

    filtered_tenant_schema = SearchTenantSchema(email="john.doe@example.com")
    filtered_tenant = TENANT_MODEL.filter_tenants(filtered_tenant_schema)
    assert len(filtered_tenant) == 1, "Filtered tenant should have one tenant."

    filtered_tenant_schema = SearchTenantSchema(email="maria.doe@example.com")
    filtered_tenant = TENANT_MODEL.filter_tenants(filtered_tenant_schema)
    assert len(filtered_tenant) == 1, "Filtered tenant should have one tenant."

    filtered_tenant_schema = SearchTenantSchema(phone="1234567890")
    filtered_tenant = TENANT_MODEL.filter_tenants(filtered_tenant_schema)
    assert len(filtered_tenant) == 1, "Filtered tenant should have one tenant."

    filtered_tenant_schema = SearchTenantSchema(phone="9876543210")
    filtered_tenant = TENANT_MODEL.filter_tenants(filtered_tenant_schema)
    assert len(filtered_tenant) == 1, "Filtered tenant should have one tenant."
