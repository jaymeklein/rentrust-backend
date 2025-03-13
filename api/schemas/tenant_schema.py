from typing import Optional

from pydantic import BaseModel, PositiveInt, EmailStr


class TenantSchema(BaseModel):
	id: Optional[PositiveInt] = None
	name: str
	id_document: str
	email: EmailStr
	phone: str
	emergency_contact: Optional[str]
	status: Optional[bool] = True

	model_config = {
		"from_attributes": True
	}


class TenantSchemaResponse(TenantSchema):
	id: PositiveInt
