from typing import Optional

from pydantic import BaseModel, PositiveInt, EmailStr, Field


class TenantSchema(BaseModel):
    id: Optional[PositiveInt] = None
    name: str | None = Field(None, min_length=5)
    id_document: str | None
    email: EmailStr | None
    phone: str | None = Field(...)
    emergency_contact: Optional[str]
    status: Optional[bool] = True

    model_config = {"from_attributes": True}


class SearchTenantSchema(TenantSchema):
    id: Optional[PositiveInt] = None
    name: Optional[str] = None
    id_document: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    emergency_contact: Optional[str] = None
    status: Optional[bool] = None


class TenantSchemaResponse(TenantSchema):
    id: Optional[PositiveInt] = None


class TenantDeleteResponse(BaseModel):
    deleted: bool
    error: Optional[str] = None
