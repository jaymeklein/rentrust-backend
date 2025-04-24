
from api.models.base.base_model import BaseModel


class PropertyModel(BaseModel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
