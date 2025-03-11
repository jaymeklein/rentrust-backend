from typing import List, Type

from api.schemas.tenant_schema import TenantCreate, Tenant
from api.services.tenant.tenant_service import TenantService


class TenantController:
	tenant_service = TenantService()

	def create_tenant(self, tenant_create: TenantCreate) -> Tenant:
		return self.tenant_service.create_tenant(tenant_create)

	def get_all_tenants(self) -> List[Tenant]:
		return self.tenant_service.get_all_tenants()

	def get_tenant(self, tenant_id: int) -> Tenant:
		return self.tenant_service.get_tenant(tenant_id)
