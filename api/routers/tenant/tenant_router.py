
from fastapi import APIRouter, HTTPException
from typing import List
from api.schemas.tenant.tenant_scheme import TenantCreate, TenantResponse
from api.services.tenant.tenant_service import TenantService

router = APIRouter()

# Dependency to inject the service
tenant_service = TenantService()


@router.get("/", response_model=List[TenantResponse])
async def list_tenants():
    return tenant_service.get_all_tenants()


@router.post("/", response_model=TenantResponse)
async def create_tenant(tenant_data: TenantCreate):
    return tenant_service.create_tenant(tenant_data)


@router.get("/{tenant_id}", response_model=TenantResponse)
async def get_tenant(tenant_id: int):
    tenant = tenant_service.get_tenant(tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


@router.put("/{tenant_id}", response_model=TenantResponse)
async def update_tenant(tenant_id: int, tenant_data: TenantCreate):
    return tenant_service.update_tenant(tenant_id, tenant_data)


@router.delete("/{tenant_id}")
async def delete_tenant(tenant_id: int):
    tenant_service.delete_tenant(tenant_id)
    return {"message": "Tenant deleted successfully"}


# routers/tenants/properties.py (if subroutes are needed for properties associated with tenants)
# @router.get("/{tenant_id}/properties", response_model=List[PropertyResponse])
# async def list_tenant_properties(tenant_id: int):
#     return tenant_service.get_tenant_properties(tenant_id)
