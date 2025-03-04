from pydantic import BaseModel, PositiveInt, EmailStr


class Tenant(BaseModel):
    id: PositiveInt
    name: str
    email: EmailStr
    phone: str

    model_config = {
        "from_attributes": True
    }


class TenantCreate(Tenant):
    pass


class TenantResponse(Tenant):
    pass
