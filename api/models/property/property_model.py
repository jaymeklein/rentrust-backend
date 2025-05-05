from typing import List

from sqlalchemy.orm import Session

from api.models.base.base_model import BaseModel
from api.schemas.property.property_schema import (
    CreatePropertySchema,
    UpdatePropertySchema,
)
from db.schemas.property.property_schema import DBProperty


class PropertyModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_property(
        self, session: Session, property_data: CreatePropertySchema
    ) -> DBProperty:
        new_property = DBProperty(**property_data.__dict__)
        session.add(new_property)
        session.commit()
        session.refresh(new_property)
        return new_property

    def get_all_properties(
        self, session: Session, only_active: bool = True
    ) -> List[DBProperty] | None:
        query = session.query(DBProperty)

        if only_active:
            query = query.filter(DBProperty.is_active)

        return query.all()

    def get_property(self, session: Session, property_id: int) -> DBProperty:
        return session.query(DBProperty).filter(DBProperty.id == property_id).first()

    def update_property(
        self, session: Session, property: DBProperty, property_data: UpdatePropertySchema
    ) -> DBProperty:
        property.update_from_model(model=property_data)
        session.commit()
        session.refresh(property)
        return property
