from typing import List

from pydantic import PositiveInt

from api.exceptions.tenant_exceptions import TenantAlreadyExistsException, TenantNotFoundException
from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant_schema import TenantSchema
from db.schemas.tenant.tenant_schema import Tenant


class TenantService:
	tenant_model = TenantModel()

	def create_tenant(self, tenant_data: TenantSchema) -> TenantSchema:
		existing_tenant = self.tenant_model.tenant_exists(tenant_data)

		if existing_tenant:
			raise TenantAlreadyExistsException(f"Tenant with specified data already exists")

		tenant = self.tenant_model.create_tenant(tenant_data).__dict__
		return TenantSchema(**tenant)

	def get_all_tenants(self) -> List[TenantSchema]:
		tenants = self.tenant_model.get_all_tenants()
		return [TenantSchema(**tenant.__dict__) for tenant in tenants]

	def get_tenant(self, tenant_id: int) -> Tenant:
		tenant = self.tenant_model.get_tenant(tenant_id)

		if not tenant:
			raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

		return tenant

	def update_tenant(self, tenant_id: PositiveInt, tenant_data: TenantSchema) -> TenantSchema:
		all_tenants = self.tenant_model.tenant_exists(tenant_data)
		if len(all_tenants) > 1:
			raise TenantAlreadyExistsException(f"Tenant with specified data already exists")

		updated_tenant = self.tenant_model.update_tenant(tenant_id, tenant_data).__dict__
		return TenantSchema(**updated_tenant)
