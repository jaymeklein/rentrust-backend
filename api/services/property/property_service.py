from api.models.property.property_model import PropertyModel
from api.services.base.base_service import BaseService
from api.schemas.property.property_schema import CreatePropertySchema, PropertySchema
from typing import List
from api.exceptions.property_exceptions import PropertyNotFoundException
from pydantic import TypeAdapter
from pickle import GET
from api.schemas.property.property_schema import UpdatePropertySchema

class PropertyService(BaseService):

	# Models
	property_model = PropertyModel()

	# Type Adapters
	property_list_adapter = TypeAdapter(List[PropertySchema])

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def create_property(self, property_data: CreatePropertySchema) -> PropertySchema:
		property = self.property_model.create_property(property_data)
		return PropertySchema(**property.as_dict())

	def list_properties(self, only_active: bool = True) -> List[PropertySchema]:
		properties = self.property_model.get_all_properties(only_active)
		properties = [property.as_dict() for property in properties]
		return self.property_list_adapter.validate_python(properties)

	def get_property(self, property_id: int) -> PropertySchema:
		property = self.property_model.get_property(property_id)

		if not property:
			raise PropertyNotFoundException(f"Property with id {property_id} not found")

		return PropertySchema(**property.as_dict())

	def update_property(self, property_id: int, property_data: UpdatePropertySchema) -> PropertySchema:
		property = self.property_model.get_property(property_id)

		if not property:
			raise PropertyNotFoundException(f"Property with id {property_id} not found")

		property = self.property_model.update_property(property_id, property_data)
		return PropertySchema(**property.as_dict())
