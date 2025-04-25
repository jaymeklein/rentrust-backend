from api.models.property.property_model import PropertyModel
from api.services.base.base_service import BaseService
from api.schemas.property.property_schema import CreatePropertySchema, PropertySchema


class PropertyService(BaseService):
	property_model = PropertyModel()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def create_property(self, property_data: CreatePropertySchema) -> PropertySchema:
		return self.property_model.create_property(property_data)
