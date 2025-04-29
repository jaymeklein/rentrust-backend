from typing import List

from fastapi import APIRouter
from pydantic import PositiveInt

from api.controllers.tenant.tenant_controller import TenantController
from api.schemas.tenant.tenant_schema import (
    SearchTenantSchema,
    TenantDeleteResponse,
    TenantSchema,
    TenantSchemaResponse,
)

router = APIRouter(prefix="/tenants")

tenant_controller = TenantController()


@router.post(path="/", response_model=TenantSchemaResponse)
async def create_tenant(tenant_data: TenantSchema):
    return tenant_controller.create_tenant(tenant_data)


@router.get(path="/", response_model=List[TenantSchemaResponse])
async def list_tenants():
    return tenant_controller.get_all_tenants()


@router.get(path="/{tenant_id}", response_model=TenantSchemaResponse)
async def get_tenant(tenant_id: PositiveInt):
    return tenant_controller.get_tenant(tenant_id)


@router.patch(path="/{tenant_id}", response_model=TenantSchemaResponse)
async def update_tenant(tenant_id: PositiveInt, tenant_data: TenantSchema):
    return tenant_controller.update_tenant(tenant_id, tenant_data)


@router.delete(path="/{tenant_id}", response_model=TenantDeleteResponse)
def delete_tenant(tenant_id: PositiveInt):
    return tenant_controller.delete_tenant(tenant_id)


@router.post(path="/search", response_model=List[TenantSchemaResponse])
async def search_properties(tenant_data: SearchTenantSchema):
    return tenant_controller.search_tenants(tenant_data)
