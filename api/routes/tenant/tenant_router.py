from fastapi import APIRouter
from typing import List

from pydantic import PositiveInt

from api.controllers.tenant.tenant_controller import TenantController
from api.schemas.tenant_schema import TenantSchema, TenantSchemaResponse, TenantDeleteResponse

router = APIRouter()

# Dependency to inject the service
tenant_controller = TenantController()


@router.post("/", response_model=TenantSchemaResponse)
async def create_tenant(tenant_data: TenantSchema):
	return tenant_controller.create_tenant(tenant_data)


@router.get("/", response_model=List[TenantSchemaResponse])
async def list_tenants():
	return tenant_controller.get_all_tenants()


@router.get("/{tenant_id}", response_model=TenantSchemaResponse)
async def get_tenant(tenant_id: PositiveInt):
	return tenant_controller.get_tenant(tenant_id)


@router.put("/{tenant_id}", response_model=TenantSchemaResponse)
async def update_tenant(tenant_id: PositiveInt, tenant_data: TenantSchema):
	return tenant_controller.update_tenant(tenant_id, tenant_data)


@router.delete("/{tenant_id}", response_model=TenantDeleteResponse)
async def delete_tenant(tenant_id: PositiveInt):
	return tenant_controller.delete_tenant(tenant_id)
