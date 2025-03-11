from api.exceptions.tenant_exceptions import TenantAlreadyExistsException
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
