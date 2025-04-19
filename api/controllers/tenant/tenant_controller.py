from typing import Type

from pydantic.v1 import PositiveInt

from api.schemas.tenant_schema import FilterTenantSchema, TenantSchema, TenantDeleteResponse
from api.services.tenant.tenant_service import TenantService
from db.schemas.tenant.tenant_schema import Tenant


class TenantController:
	tenant_service = TenantService()

	def create_tenant(self, tenant_data: TenantSchema) -> Tenant:
		return self.tenant_service.create_tenant(tenant_data)

	def get_all_tenants(self) -> list[Type[Tenant]]:
		return self.tenant_service.get_all_tenants()

	def get_tenant(self, tenant_id: PositiveInt) -> Tenant:
		return self.tenant_service.get_tenant(tenant_id)

	def update_tenant(self, tenant_id: PositiveInt, tenant_data: TenantSchema) -> Type[Tenant] | None:
		return self.tenant_service.update_tenant(tenant_id, tenant_data)

	def delete_tenant(self, tenant_id: PositiveInt) -> TenantDeleteResponse:
		return self.tenant_service.delete_tenant(tenant_id)

	def filter_tenants(self, tenant_data: FilterTenantSchema) -> list[Type[Tenant]]:
		return self.tenant_service.filter_tenants(tenant_data)