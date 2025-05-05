from typing import List

from sqlalchemy.orm import Session

from api.decorators.inject_db_session import with_session
from api.models.base.base_model import BaseModel
from api.schemas.property.property_schema import (
    CreatePropertySchema,
    UpdatePropertySchema,
)
from db.schemas.property.property_schema import DBProperty


class PropertyModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @with_session
    def create_property(
        self, session: Session, property_data: CreatePropertySchema
    ) -> DBProperty:
        new_property = DBProperty(**property_data.__dict__)
        session.add(new_property)
        session.commit()
        session.refresh(new_property)
        return new_property

    @with_session
    def get_all_properties(
        self, session: Session, only_active: bool = True
    ) -> List[DBProperty] | None:
        query = session.query(DBProperty)

        if only_active:
            query = query.filter(DBProperty.is_active)

        return query.all()

    @with_session
    def get_property(self, session: Session, property_id: int) -> DBProperty:
        return session.query(DBProperty).filter(DBProperty.id == property_id).first()

    @with_session
    def update_property(
        self, session: Session, property: DBProperty, property_data: UpdatePropertySchema
    ) -> DBProperty:
        property.update_from_model(model=property_data)
        session.commit()
        session.refresh(property)
        return property
