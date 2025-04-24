from fastapi import APIRouter
from api.controllers.property.property_controller import PropertyController

router = APIRouter(prefix='/properties')
property_controller = PropertyController()

@router.post(path='/')
async def create_property(property_data):
	"""Todo: Implement create_property"""
	pass

@router.get(path='/')
async def list_properties():
	"""Todo: Implement list_properties"""
	pass

@router.get(path='/{property_id}')
async def get_property(property_id):
	"""Todo: Implement get_property"""
	pass

@router.patch(path='/{property_id}')
async def update_property(property_id, property_data):
	"""Todo: Implement update_property"""
	pass

@router.delete(path='/{property_id}')
async def delete_property(property_id):
	"""Todo: Implement delete_property"""
	pass

@router.post(path="/search")
async def search_properties(filter_data):
	"""Todo: Implement search_properties"""
	pass
