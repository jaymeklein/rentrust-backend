from api.schemas.property.property_schema import CreatePropertySchema, PropertySchema
from api.controllers.base.base_controller import BaseController
from api.services.property.property_service import PropertyService

class PropertyController(BaseController):
	property_service = PropertyService()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def create_property(self, property_data: CreatePropertySchema) -> PropertySchema:
		return self.property_service.create_property(property_data)
