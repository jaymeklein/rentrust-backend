from pydantic import PositiveInt
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from api.models.base.base_model import BaseModel
from api.schemas.tenant.tenant_schema import (
    SearchTenantSchema,
    TenantDeleteResponse,
)
from api.schemas.tenant.tenant_schema import (
    TenantSchema as TenantSchema,
)
from db.schemas.tenant.tenant_schema import DBTenant


class TenantModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_all_tenants(
        self, session: Session, get_inactive: bool = False
    ) -> list[DBTenant]:
        query = session.query(DBTenant)

        if not get_inactive:
            query = query.filter(DBTenant.status)

        return query.all()

    def create_tenant(self, session: Session, tenant_data: TenantSchema) -> DBTenant:
        new_tenant = DBTenant(**tenant_data.__dict__)
        session.add(new_tenant)
        session.commit()
        session.refresh(new_tenant)
        return new_tenant

    def get_tenant(self, session: Session, tenant_id: PositiveInt) -> DBTenant | None:
        return session.query(DBTenant).filter(DBTenant.id == tenant_id).first()

    def update_tenant(
        self, session: Session, db_tenant: DBTenant, tenant_data: DBTenant
    ) -> DBTenant | None:
        db_tenant.update_from_model(model=tenant_data)
        session.commit()
        session.refresh(db_tenant)
        return db_tenant

    def delete_tenant(self, session: Session, tenant: DBTenant) -> TenantDeleteResponse:
        tenant_delete_response = TenantDeleteResponse(deleted=True)

        try:
            session.query(DBTenant).filter_by(id=tenant.id).delete()
            session.commit()
            return tenant_delete_response

        except Exception as e:
            tenant_delete_response.error = str(e)
            tenant_delete_response.deleted = False
            return tenant_delete_response

    def tenant_exists(
        self, session: Session, tenant_data: TenantSchema
    ) -> list[DBTenant]:
        return (
            session.query(DBTenant).filter(
                or_(
                    DBTenant.email == tenant_data.email,
                    DBTenant.phone == tenant_data.phone,
                    DBTenant.id_document == tenant_data.id_document,
                )
            )
        ).all()

    def truncate_tenants(self, session: Session) -> None:
        if not self.testing:
            raise ValueError("Cannot truncate tenants without testing mode")

        session.query(DBTenant).delete()
        session.commit()

    def filter_tenants(
        self, session: Session, tenant_data: SearchTenantSchema
    ) -> list[DBTenant]:
        query = session.query(DBTenant)
        filters = []

        if tenant_data.id:
            filters.append(DBTenant.id == tenant_data.id)

        if tenant_data.email:
            filters.append(DBTenant.email == tenant_data.email)

        if tenant_data.name:
            filters.append(DBTenant.name.like(f"%{tenant_data.name}%"))

        if tenant_data.id_document:
            filters.append(DBTenant.id_document == tenant_data.id_document)

        if tenant_data.phone:
            filters.append(DBTenant.phone == tenant_data.phone)

        if tenant_data.emergency_contact:
            filters.append(DBTenant.emergency_contact == tenant_data.emergency_contact)

        return query.filter(and_(*filters)).all()
