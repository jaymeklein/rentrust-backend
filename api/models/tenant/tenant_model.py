from typing import Type

from pydantic import PositiveInt
from sqlalchemy import or_
from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.exceptions.tenant_exceptions import TenantNotFoundException
from api.schemas.tenant_schema import TenantSchema as TenantSchema, TenantDeleteResponse
from db.schemas.tenant.tenant_schema import Tenant


class TenantModel:

	@classmethod
	@with_session
	def get_all_tenants(cls, session: Session) -> list[Type[Tenant]]:
		return (
			session
			.query(Tenant)
			.filter(Tenant.status)
			.all()
		)

	@classmethod
	@with_session
	def create_tenant(cls, session: Session, tenant_data: TenantSchema) -> Tenant:
		new_tenant = Tenant(**tenant_data.__dict__)
		session.add(new_tenant)
		session.commit()
		session.refresh(new_tenant)
		return new_tenant

	@classmethod
	@with_session
	def get_tenant(cls, session: Session, tenant_id: PositiveInt) -> Tenant | None:
		return session.query(Tenant).filter(Tenant.id == tenant_id).first()

	@classmethod
	@with_session
	def update_tenant(cls, session: Session, tenant_id: PositiveInt, tenant_data: TenantSchema) -> Type[Tenant] | None:
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

	@classmethod
	@with_session
	def delete_tenant(cls, session: Session, tenant: Tenant) -> TenantDeleteResponse:
		tenant_delete_response = TenantDeleteResponse(deleted=True)

		try:
			session.delete(tenant)
			session.commit()
			return tenant_delete_response

		except Exception as e:
			tenant_delete_response.error = str(e)
			tenant_delete_response.deleted = False
			return tenant_delete_response

	@classmethod
	@with_session
	def tenant_exists(cls, session: Session, tenant_data: TenantSchema) -> list[Type[Tenant]]:
		return (
			session
			.query(Tenant)
			.filter(
				or_(Tenant.email == tenant_data.email,
					Tenant.phone == tenant_data.phone,
					Tenant.id_document == tenant_data.id_document)
			)
		).all()
