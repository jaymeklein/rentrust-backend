from typing import List, Type

from pydantic import PositiveInt
from sqlalchemy.orm import Session

from api.exceptions.tenant_exceptions import (
    EmptyTenantFilterException,
    TenantAlreadyExistsException,
    TenantNotFoundException,
)
from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant.tenant_schema import (
    SearchTenantSchema,
    TenantDeleteResponse,
    TenantSchema,
)
from api.services.base.base_service import BaseService
from db.schemas.tenant.tenant_schema import DBTenant


class TenantService(BaseService):
    tenant_model = TenantModel()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tenant(self, session: Session, tenant_data: TenantSchema) -> DBTenant:
        existing_tenant = self.tenant_model.tenant_exists(session, tenant_data)

        if existing_tenant:
            raise TenantAlreadyExistsException(
                "Tenant with specified data already exists"
            )

        return self.tenant_model.create_tenant(session, tenant_data)

    def get_all_tenants(self, session: Session) -> list[Type[DBTenant]]:
        return self.tenant_model.get_all_tenants(session)

    def get_tenant(self, session: Session, tenant_id: int) -> DBTenant:
        tenant = self.tenant_model.get_tenant(session, tenant_id)

        if not tenant:
            raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

        return tenant

    def update_tenant(
        self, session: Session, tenant_id: PositiveInt, tenant_data: TenantSchema
    ) -> Type[DBTenant]:
        all_tenants = self.tenant_model.tenant_exists(session, tenant_data)
        if len(all_tenants) > 1:
            raise TenantAlreadyExistsException(
                "Tenant with specified data already exists"
            )

        elif len(all_tenants) == 0:
            raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

        return self.tenant_model.update_tenant(session, all_tenants[0], tenant_data)

    def delete_tenant(self, session: Session, tenant_id: PositiveInt) -> TenantDeleteResponse:
        tenant = self.tenant_model.get_tenant(session, tenant_id)

        if not tenant:
            raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

        return self.tenant_model.delete_tenant(session, tenant)

    def search_tenants(self, session: Session, tenant_data: SearchTenantSchema) -> List[Type[DBTenant]]:
        filter_data = tenant_data.model_dump()
        if not any(filter_data.values()):
            raise EmptyTenantFilterException(
                "Tenant filter must have at least one value"
            )

        return self.tenant_model.filter_tenants(session, tenant_data)
