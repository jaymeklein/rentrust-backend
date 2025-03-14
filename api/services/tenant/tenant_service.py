from typing import List, Type

from pydantic import PositiveInt

from api.exceptions.tenant_exceptions import TenantAlreadyExistsException, TenantNotFoundException
from api.models.tenant.tenant_model import TenantModel
from api.schemas.tenant_schema import TenantSchema, TenantDeleteResponse
from db.schemas.tenant.tenant_schema import Tenant


class TenantService:
	tenant_model = TenantModel()

	def create_tenant(self, tenant_data: TenantSchema) -> Tenant:
		existing_tenant = self.tenant_model.tenant_exists(tenant_data)

		if existing_tenant:
			raise TenantAlreadyExistsException(f"Tenant with specified data already exists")

		return self.tenant_model.create_tenant(tenant_data)

	def get_all_tenants(self) -> list[Type[Tenant]]:
		return self.tenant_model.get_all_tenants()

	def get_tenant(self, tenant_id: int) -> Tenant:
		tenant = self.tenant_model.get_tenant(tenant_id)

		if not tenant:
			raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

		return tenant

	def update_tenant(self, tenant_id: PositiveInt, tenant_data: TenantSchema) -> Type[Tenant] | None:
		all_tenants = self.tenant_model.tenant_exists(tenant_data)
		if len(all_tenants) > 1:
			raise TenantAlreadyExistsException(f"Tenant with specified data already exists")

		return self.tenant_model.update_tenant(tenant_id, tenant_data)

	def delete_tenant(self, tenant_id: PositiveInt) -> TenantDeleteResponse:
		tenant = self.tenant_model.get_tenant(tenant_id)

		if not tenant:
			raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

		return self.tenant_model.delete_tenant(tenant)
