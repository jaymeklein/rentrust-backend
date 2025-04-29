
from pydantic import PositiveInt
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.exceptions.tenant_exceptions import TenantNotFoundException
from api.schemas.tenant.tenant_schema import SearchTenantSchema, TenantSchema as TenantSchema, TenantDeleteResponse
from api.models.base.base_model import BaseModel
from db.schemas.tenant.tenant_schema import Tenant


class TenantModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @with_session
    def get_all_tenants(
        self, session: Session, get_inactive: bool = False
    ) -> list[Tenant]:
        query = session.query(Tenant)

        if not get_inactive:
            query = query.filter(Tenant.status)

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
    def update_tenant(
        self, session: Session, tenant_id: PositiveInt, tenant_data: TenantSchema
    ) -> Tenant | None:
        tenant = session.query(Tenant).filter(Tenant.id == tenant_id).first()
        if not tenant:
            raise TenantNotFoundException(f"Tenant with id {tenant_id} not found")

        ignored_keys = ["id"]
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
            session.query(Tenant).filter_by(id=tenant.id).delete()
            session.commit()
            return tenant_delete_response

        except Exception as e:
            tenant_delete_response.error = str(e)
            tenant_delete_response.deleted = False
            return tenant_delete_response

    @with_session
    def tenant_exists(
        self, session: Session, tenant_data: TenantSchema
    ) -> list[Tenant]:
        return (
            session.query(Tenant).filter(
                or_(
                    Tenant.email == tenant_data.email,
                    Tenant.phone == tenant_data.phone,
                    Tenant.id_document == tenant_data.id_document,
                )
            )
        ).all()

    @with_session
    def truncate_tenants(self, session: Session) -> None:
        if not self.testing:
            raise ValueError("Cannot truncate tenants without testing mode")

        session.query(Tenant).delete()
        session.commit()

    @with_session
    def filter_tenants(
    self, session: Session, tenant_data: SearchTenantSchema
    ) -> list[Tenant]:
        query = session.query(Tenant)
        filters = []

        if tenant_data.id:
            filters.append(Tenant.id == tenant_data.id)

        if tenant_data.email:
            filters.append(Tenant.email == tenant_data.email)

        if tenant_data.name:
            filters.append(Tenant.name.like(f"%{tenant_data.name}%"))

        if tenant_data.id_document:
            filters.append(Tenant.id_document == tenant_data.id_document)

        if tenant_data.phone:
            filters.append(Tenant.phone == tenant_data.phone)

        if tenant_data.emergency_contact:
            filters.append(Tenant.emergency_contact == tenant_data.emergency_contact)

        return query.filter(and_(*filters)).all()
