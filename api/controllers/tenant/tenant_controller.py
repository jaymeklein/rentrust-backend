from typing import Type

from pydantic import PositiveInt, TypeAdapter
from sqlalchemy.orm import Session
from api.controllers.base.base_controller import BaseController
from api.schemas.tenant.tenant_schema import (
    SearchTenantSchema,
    TenantDeleteResponse,
    TenantSchema,
)
from api.services.tenant.tenant_service import TenantService
from db.schemas.tenant.tenant_schema import DBTenant


class TenantController(BaseController):
    tenant_service = TenantService()

    tenant_list_adapter = TypeAdapter(list[TenantSchema])
    tenant_adapter = TypeAdapter(TenantSchema)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tenant(self, session: Session, tenant_data: TenantSchema) -> TenantSchema:
        tenant = self.tenant_service.create_tenant(session, tenant_data)
        return self.tenant_adapter.validate_python(tenant.as_dict())

    def get_all_tenants(self, session: Session) -> list[TenantSchema]:
        tenants = self.tenant_service.get_all_tenants(session)
        tenants = [tenant.as_dict() for tenant in tenants]
        return self.tenant_list_adapter.validate_python(tenants)

    def get_tenant(self, session: Session, tenant_id: PositiveInt) -> TenantSchema:
        tenant = self.tenant_service.get_tenant(session, tenant_id)
        return self.tenant_adapter.validate_python(tenant.as_dict())

    def update_tenant(
        self, session: Session, tenant_id: PositiveInt, tenant_data: TenantSchema
    ) -> TenantSchema:
        tenant = self.tenant_service.update_tenant(session, tenant_id, tenant_data)
        return self.tenant_adapter.validate_python(tenant.as_dict())

    def delete_tenant(self, session: Session, tenant_id: PositiveInt) -> TenantDeleteResponse:
        return self.tenant_service.delete_tenant(session, tenant_id)

    def search_tenants(self, session: Session, tenant_data: SearchTenantSchema) -> list[Type[DBTenant]]:
        return self.tenant_service.search_tenants(session, tenant_data)
