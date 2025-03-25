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

	model_config = {
		"from_attributes": True
	}


class TenantSchemaResponse(TenantSchema):
	id: PositiveInt


class TenantDeleteResponse(BaseModel):
	deleted: bool
	error: Optional[str] = None
