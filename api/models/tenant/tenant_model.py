from typing import List, Type

from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from db.engine import get_engine
from api.schemas.tenant_schema import TenantCreate
from db.schemas.tenant.tenant_model import Tenant


class TenantModel:
	def get_all_tenants(self) -> List[Type[Tenant]]:
		with Session(get_engine()) as session:
			return (
				session
				.query(Tenant)
				.all()
			)

	def create_tenant(self, tenant_data: TenantCreate) -> Tenant:
		new_tenant = Tenant(**tenant_data.__dict__)
		with Session(get_engine()) as session:
			session.add(new_tenant)
			session.commit()
			session.refresh(new_tenant)
			return new_tenant

	def get_tenant(self, tenant_id: int) -> Tenant | None:
		with Session(get_engine()) as session:
			return session.query(Tenant).filter(Tenant.id == tenant_id).first()

	def update_tenant(self, tenant_id: int, tenant_data: TenantCreate) -> Tenant:
		tenant = self.get_tenant(tenant_id)
		if not tenant:
			raise HTTPException(status_code=404, detail="Tenant not found")

		for key, value in tenant_data.__dict__.items():
			setattr(tenant, key, value)

		with Session(get_engine()) as session:
			session.commit()
			session.refresh(tenant)

		return tenant

	def delete_tenant(self, tenant_id: int):
		tenant = self.get_tenant(tenant_id)
		if not tenant:
			raise HTTPException(status_code=404, detail="Tenant not found")

		with Session(get_engine()) as session:
			session.delete(tenant)
			session.commit()

	def tenant_exists(self, tenant_data: TenantCreate) -> Tenant | None:
		with (Session(get_engine()) as session):
			return (session
			.query(Tenant)
			.filter(
				or_(Tenant.email == tenant_data.email,
					 Tenant.phone == tenant_data.phone,
					 Tenant.id_document == tenant_data.id_document)
			)).first()
