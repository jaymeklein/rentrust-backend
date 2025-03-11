from typing import List, Type

from api.exceptions.tenant_exceptions import TenantAlreadyExistsException, TenantNotFoundException
from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant_schema import Tenant, TenantCreate


class TenantService:
	tenant_model = TenantModel()

	def create_tenant(self, tenant_create: TenantCreate) -> Tenant:
		existing_tenant = self.tenant_model.tenant_exists(tenant_create)

		if existing_tenant:
			raise TenantAlreadyExistsException(f"Tenant with specified data already exists")

		tenant = self.tenant_model.create_tenant(tenant_create).__dict__
		return Tenant(**tenant)

	def get_all_tenants(self) -> List[Tenant]:
		tenants = self.tenant_model.get_all_tenants()
		return [Tenant(**tenant.__dict__) for tenant in tenants]

	def get_tenant(self, tenant_id: int) -> Tenant:
		tenant = self.tenant_model.get_tenant(tenant_id)

		if not tenant:
			raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

		return tenant
