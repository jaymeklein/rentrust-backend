from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.controllers.property.property_controller import PropertyController
from db.engine import get_session
from api.schemas.property.property_schema import (
    CreatePropertySchema,
    PropertySchema,
    UpdatePropertySchema,
)

router = APIRouter(prefix="/properties")
property_controller = PropertyController()


@router.post(path="/", response_model=PropertySchema)
async def create_property(property_data: CreatePropertySchema, session: Session = Depends(get_session)):
    return property_controller.create_property(session, property_data)


@router.get(path="/", response_model=List[PropertySchema])
async def list_properties(only_active: bool = True, session: Session = Depends(get_session)):
    return property_controller.list_properties(session, only_active)


@router.get(path="/{property_id}", response_model=PropertySchema)
async def get_property(property_id, session: Session = Depends(get_session)):
    return property_controller.get_property(session, property_id)


@router.patch(path="/{property_id}", response_model=PropertySchema)
async def update_property(property_id, property_data: UpdatePropertySchema, session: Session = Depends(get_session)):
    return property_controller.update_property(session, property_id, property_data)


@router.delete(path="/{property_id}")
async def delete_property(property_id):
    """Todo: Implement delete_property"""
    pass


@router.post(path="/search", response_model=List[PropertySchema])
async def search_properties(filter_data):
    """Todo: Implement search_properties"""
    pass
