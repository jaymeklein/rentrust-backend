from typing import List

from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.models.base.base_model import BaseModel
from api.schemas.property.property_schema import (
    CreatePropertySchema,
    UpdatePropertySchema,
)
from db.schemas.property.property_model import Property


class PropertyModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @with_session
    def create_property(
        self, session: Session, property_data: CreatePropertySchema
    ) -> Property:
        new_property = Property(**property_data.__dict__)
        session.add(new_property)
        session.commit()
        session.refresh(new_property)
        return new_property

    @with_session
    def get_all_properties(
        self, session: Session, only_active: bool = True
    ) -> List[Property] | None:
        query = session.query(Property)

        if only_active:
            query = query.filter(Property.is_active)

        return query.all()

    @with_session
    def get_property(self, session: Session, property_id: int) -> Property:
        return session.query(Property).filter(Property.id == property_id).first()

    @with_session
    def update_property(
        self, session: Session, property: Property, property_data: UpdatePropertySchema
    ) -> Property:
        ignored_keys = ["id"]
        for key, value in property_data.__dict__.items():
            if key not in ignored_keys:
                setattr(property, key, value)

        session.commit()
        session.refresh(property)
        return property
