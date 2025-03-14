from typing import List, Type

from fastapi import HTTPException
from pydantic import PositiveInt
from sqlalchemy import or_
from sqlalchemy.orm import Session

from api.exceptions.tenant_exceptions import TenantNotFoundException
from db.engine import get_engine
from api.schemas.tenant_schema import TenantSchema as TenantSchema, TenantDeleteResponse
from db.schemas.tenant.tenant_schema import Tenant


class TenantModel:
	def get_all_tenants(self) -> list[Type[Tenant]]:
		with Session(get_engine()) as session:
			return (
				session
				.query(Tenant)
				.filter(Tenant.status)
				.all()
			)

	def create_tenant(self, tenant_data: TenantSchema) -> Tenant:
		new_tenant = Tenant(**tenant_data.__dict__)
		with Session(get_engine()) as session:
			session.add(new_tenant)
			session.commit()
			session.refresh(new_tenant)
			return new_tenant

	def get_tenant(self, tenant_id: PositiveInt) -> Tenant | None:
		with Session(get_engine()) as session:
			return session.query(Tenant).filter(Tenant.id == tenant_id).first()

	def update_tenant(self, tenant_id: PositiveInt, tenant_data: TenantSchema) -> Type[Tenant] | None:
		with Session(get_engine()) as session:
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

	def delete_tenant(self, tenant: Tenant) -> TenantDeleteResponse:
		tenant_delete_response = TenantDeleteResponse(deleted=True)

		try:
			with Session(get_engine()) as session:
				session.delete(tenant)
				session.commit()
				return tenant_delete_response

		except Exception as e:
			tenant_delete_response.error = str(e)
			tenant_delete_response.deleted = False
			return tenant_delete_response



	def tenant_exists(self, tenant_data: TenantSchema) -> list[Type[Tenant]]:
		with (
			Session(get_engine()) as session):
			return (
				session
				.query(Tenant)
				.filter(
					or_(Tenant.email == tenant_data.email,
						Tenant.phone == tenant_data.phone,
						Tenant.id_document == tenant_data.id_document)
				)
			).all()
