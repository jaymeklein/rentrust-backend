from typing import Optional

from pydantic import BaseModel, PositiveInt, EmailStr, Field


class TenantSchema(BaseModel):
    id: Optional[PositiveInt] = None
    name: str = Field(..., min_length=5)
    id_document: str
    email: EmailStr
    phone: str = Field(...)
    emergency_contact: Optional[str]
    status: Optional[bool] = True

    model_config = {"from_attributes": True}


class FilterTenantSchema(TenantSchema):
    id: Optional[PositiveInt] = None
    name: Optional[str] = Field(None)
    id_document: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    emergency_contact: Optional[str] = None
    status: Optional[bool] = None


class TenantSchemaResponse(TenantSchema):
    id: PositiveInt


class TenantDeleteResponse(BaseModel):
    deleted: bool
    error: Optional[str] = None
