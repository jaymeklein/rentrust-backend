from fastapi import APIRouter
from api.controllers.property.property_controller import PropertyController
from api.schemas.property.property_schema import PropertySchema
from typing import List
from api.schemas.property.property_schema import CreatePropertySchema
from api.schemas.property.property_schema import UpdatePropertySchema

router = APIRouter(prefix='/properties')
property_controller = PropertyController()

@router.post(path='/', response_model=PropertySchema)
async def create_property(property_data: CreatePropertySchema):
	return property_controller.create_property(property_data)

@router.get(path='/', response_model=List[PropertySchema])
async def list_properties(only_active: bool = True):
	return property_controller.list_properties(only_active)

@router.get(path='/{property_id}', response_model=PropertySchema)
async def get_property(property_id):
	return property_controller.get_property(property_id)

@router.patch(path='/{property_id}', response_model=PropertySchema)
async def update_property(property_id, property_data: UpdatePropertySchema):
	return property_controller.update_property(property_id, property_data)

@router.delete(path='/{property_id}')
async def delete_property(property_id):
	"""Todo: Implement delete_property"""
	pass

@router.post(path="/search", response_model=List[PropertySchema])
async def search_properties(filter_data):
	"""Todo: Implement search_properties"""
	pass
