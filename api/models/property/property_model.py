from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.models.base.base_model import BaseModel
from db.schemas.property.property_model import Property
from api.schemas.property.property_schema import CreatePropertySchema

class PropertyModel(BaseModel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	@with_session
	def create_property(self, session: Session, property_data: CreatePropertySchema) -> Property:
		new_property = Property(**property_data.__dict__)
		session.add(new_property)
		session.commit()
		session.refresh(new_property)
		return new_property
