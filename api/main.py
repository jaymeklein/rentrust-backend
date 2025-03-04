from fastapi import FastAPI
from routers.tenant import tenant_router

app = FastAPI()

app.include_router(tenant_router.router, prefix="/tenants", tags=["Tenants"])
# app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
# app.include_router(properties.router, prefix="/properties", tags=["Properties"])
# app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
