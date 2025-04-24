from fastapi import FastAPI
from api.routes.tenant import tenant_router
from api.routes.property import property_router

app = FastAPI()

app.include_router(tenant_router.router, tags=["Tenants"])
app.include_router(property_router.router, tags=["Properties"])
# app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
