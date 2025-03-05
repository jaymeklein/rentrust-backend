from pydantic import BaseModel, PositiveInt, EmailStr


class Tenant(BaseModel):
    id: PositiveInt
    name: str
    email: EmailStr
    phone: str
    emergency_contact: str | None

    model_config = {
        "from_attributes": True
    }


class TenantCreate(Tenant):
    id: None


class TenantResponse(Tenant):
    id: PositiveInt 

