from fastapi import APIRouter, HTTPException
from typing import List

from api.controllers.tenant.tenant_controller import TenantController
from api.schemas.tenant_schema import TenantCreate, TenantResponse

router = APIRouter()

# Dependency to inject the service
tenant_controller = TenantController()


@router.post("/", response_model=TenantResponse)
async def create_tenant(tenant_data: TenantCreate):
	return tenant_controller.create_tenant(tenant_data)


@router.get("/", response_model=List[TenantResponse])
async def list_tenants():
	return tenant_controller.get_all_tenants()


@router.get("/{tenant_id}", response_model=TenantResponse)
async def get_tenant(tenant_id: int):
	tenant = tenant_controller.get_tenant(tenant_id)
	if not tenant:
		raise HTTPException(status_code=404, detail="Tenant not found")
	return tenant


@router.put("/{tenant_id}", response_model=TenantResponse)
async def update_tenant(tenant_id: int, tenant_data: TenantCreate):
	return tenant_controller.update_tenant(tenant_id, tenant_data)


@router.delete("/{tenant_id}")
async def delete_tenant(tenant_id: int):
	tenant_controller.delete_tenant(tenant_id)
	return {"message": "Tenant deleted successfully"}
