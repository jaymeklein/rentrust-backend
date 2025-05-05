from typing import List

from sqlalchemy.orm import Session

from api.controllers.base.base_controller import BaseController
from api.schemas.property.property_schema import (
    CreatePropertySchema,
    PropertySchema,
    UpdatePropertySchema,
)
from api.services.property.property_service import PropertyService


class PropertyController(BaseController):
    property_service = PropertyService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_property(self, session: Session, property_data: CreatePropertySchema) -> PropertySchema:
        return self.property_service.create_property(session, property_data)

    def list_properties(self, session: Session, only_active: bool = True) -> List[PropertySchema]:
        return self.property_service.list_properties(session, only_active)

    def get_property(self, session: Session, property_id: int) -> PropertySchema:
        return self.property_service.get_property(session, property_id)

    def update_property(
        self, session: Session, property_id: int, property_data: UpdatePropertySchema
    ) -> PropertySchema:
        return self.property_service.update_property(session, property_id, property_data)
