from typing import List, Type

from pydantic.v1 import PositiveInt

from api.schemas.tenant_schema import TenantSchema
from api.services.tenant.tenant_service import TenantService
from db.schemas.tenant.tenant_schema import Tenant


class TenantController:
	tenant_service = TenantService()

	def create_tenant(self, tenant_data: TenantSchema) -> TenantSchema:
		return self.tenant_service.create_tenant(tenant_data)

	def get_all_tenants(self) -> List[TenantSchema]:
		return self.tenant_service.get_all_tenants()

	def get_tenant(self, tenant_id: PositiveInt) -> Tenant:
		return self.tenant_service.get_tenant(tenant_id)

	def update_tenant(self, tenant_id: PositiveInt, tenant_data: TenantSchema) -> TenantSchema:
		return self.tenant_service.update_tenant(tenant_id, tenant_data)
