from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Field, model_validator
from pydantic.types import PositiveFloat
from api.exceptions.property_exceptions import MissingUpdateFieldException

class PropertySchema(BaseModel):
	# Ids
	id: PositiveInt
	# owner_id: PositiveInt

	# Optional IDs
	tenant_id: Optional[PositiveInt] = Field(None)
	# real_estate_company_id: Optional[PositiveInt] = Field(None)

	# Main attributes
	name: str = Field(..., min_length=5)
	description: str = Field(..., min_length=5)
	size_m2: PositiveFloat
	listed_date: date
	last_updated: date

	# Optional values
	value: Optional[PositiveFloat] = Field(None)
	year_built: Optional[PositiveInt] = Field(None, le=datetime.today().year)
	is_active: bool = Field(True)


class CreatePropertySchema(PropertySchema):
	id: Optional[None] = Field(None)
	tenant_id: Optional[None] = Field(None)


class UpdatePropertySchema(PropertySchema):
	...

	@model_validator(mode='after')
	def validate_fields(cls, values):
		"""Validates existence of at least one field to update"""
		provided_fields = {key: value for key, value in values.model_dump().items() if key != 'id'}

		if len(provided_fields) == 0:
			raise MissingUpdateFieldException("No fields provided for update")

		return values
