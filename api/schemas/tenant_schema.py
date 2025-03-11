from typing import Optional

from pydantic import BaseModel, PositiveInt, EmailStr


class Tenant(BaseModel):
	id: PositiveInt
	name: str
	id_document: str
	email: EmailStr
	phone: str
	emergency_contact: Optional[str]
	status: Optional[bool] = True

	model_config = {
		"from_attributes": True
	}


class TenantCreate(Tenant):
	id: None


class TenantResponse(Tenant):
	id: PositiveInt
