from api.models.property.property_model import PropertyModel
from api.services.base.base_service import BaseService


class PropertyService(BaseService):
	property_model = PropertyModel()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
