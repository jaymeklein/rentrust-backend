from api.schemas.property.property_schema import CreatePropertySchema, PropertySchema
from api.controllers.base.base_controller import BaseController
from api.services.property.property_service import PropertyService
from typing import List
from api.schemas.property.property_schema import UpdatePropertySchema

class PropertyController(BaseController):
	property_service = PropertyService()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def create_property(self, property_data: CreatePropertySchema) -> PropertySchema:
		return self.property_service.create_property(property_data)

	def list_properties(self, only_active: bool = True) -> List[PropertySchema]:
		return self.property_service.list_properties(only_active)

	def get_property(self, property_id: int) -> PropertySchema:
		return self.property_service.get_property(property_id)

	def update_property(self, property_id: int, property_data: UpdatePropertySchema) -> PropertySchema:
		return self.property_service.update_property(property_id, property_data)
