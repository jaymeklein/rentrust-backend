from typing import List

from fastapi import APIRouter, Depends
from pydantic import PositiveInt
from sqlalchemy.orm import Session
from api.controllers.tenant.tenant_controller import TenantController
from api.schemas.tenant.tenant_schema import (
    SearchTenantSchema,
    TenantDeleteResponse,
    TenantSchema,
    TenantSchemaResponse,
)
from db.engine import get_session

router = APIRouter(prefix="/tenants")

tenant_controller = TenantController()


@router.post(path="/", response_model=TenantSchemaResponse)
async def create_tenant(tenant_data: TenantSchema, session: Session = Depends(get_session)):
    return tenant_controller.create_tenant(session, tenant_data)


@router.get(path="/", response_model=List[TenantSchemaResponse])
async def list_tenants(session: Session = Depends(get_session)):
    tenants = tenant_controller.get_all_tenants(session)
    return tenants


@router.get(path="/{tenant_id}", response_model=TenantSchemaResponse)
async def get_tenant(tenant_id: PositiveInt, session: Session = Depends(get_session)):
    return tenant_controller.get_tenant(session, tenant_id)


@router.patch(path="/{tenant_id}", response_model=TenantSchemaResponse)
async def update_tenant(tenant_id: PositiveInt, tenant_data: TenantSchema, session: Session = Depends(get_session)):
    return tenant_controller.update_tenant(session, tenant_id, tenant_data)


@router.delete(path="/{tenant_id}", response_model=TenantDeleteResponse)
def delete_tenant(tenant_id: PositiveInt, session: Session = Depends(get_session)):
    return tenant_controller.delete_tenant(session, tenant_id)


@router.post(path="/search", response_model=List[TenantSchemaResponse])
async def search_properties(tenant_data: SearchTenantSchema, session: Session = Depends(get_session)):
    return tenant_controller.search_tenants(session, tenant_data)
