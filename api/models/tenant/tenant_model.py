from typing import Type

from pydantic import PositiveInt
from sqlalchemy import or_
from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.exceptions.tenant_exceptions import TenantNotFoundException
from api.schemas.tenant_schema import TenantSchema as TenantSchema, TenantDeleteResponse
from db.schemas.tenant.tenant_schema import Tenant


class TenantModel:
	testing: bool = False

	def __init__(self, testing: bool = False):
		print(f"is testing: {testing}")
		self.testing = testing

	@with_session
	def get_all_tenants(self, session: Session, get_inactive: bool = False) -> list[Type[Tenant]]:
		query = (
			session
			.query(Tenant)
		)

		if not get_inactive:
			return query.filter(Tenant.status).all()

		return query.all()

	@with_session
	def create_tenant(self, session: Session, tenant_data: TenantSchema) -> Tenant:
		new_tenant = Tenant(**tenant_data.__dict__)
		session.add(new_tenant)
		session.commit()
		session.refresh(new_tenant)
		return new_tenant

	@with_session
	def get_tenant(self, session: Session, tenant_id: PositiveInt) -> Tenant | None:
		return session.query(Tenant).filter(Tenant.id == tenant_id).first()

	@with_session
	def update_tenant(self, session: Session, tenant_id: PositiveInt, tenant_data: TenantSchema) -> Type[Tenant] | None:
		tenant = session.query(Tenant).filter(Tenant.id == tenant_id).first()
		if not tenant:
			raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

		ignored_keys = ['id']
		for key, value in tenant_data.__dict__.items():
			if key not in ignored_keys:
				setattr(tenant, key, value)

		session.commit()
		session.refresh(tenant)

		return tenant

	@with_session
	def delete_tenant(self, session: Session, tenant: Tenant) -> TenantDeleteResponse:
		tenant_delete_response = TenantDeleteResponse(deleted=True)

		try:
			session.delete(tenant)
			session.commit()
			return tenant_delete_response

		except Exception as e:
			tenant_delete_response.error = str(e)
			tenant_delete_response.deleted = False
			return tenant_delete_response

	@with_session
	def tenant_exists(self, session: Session, tenant_data: TenantSchema) -> list[Type[Tenant]]:
		return (
			session
			.query(Tenant)
			.filter(
				or_(Tenant.email == tenant_data.email,
					Tenant.phone == tenant_data.phone,
					Tenant.id_document == tenant_data.id_document)
			)
		).all()

	@with_session
	def truncate_tenants(self, session: Session) -> None:
		if not self.testing:
			raise ValueError("Cannot truncate tenants without testing mode")

		session.query(Tenant).delete()
		session.commit()
