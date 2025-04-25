from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Field
from pydantic.types import PositiveFloat

from api.utils.property_enums import PropertyStatus, PropertyType

class PropertySchema(BaseModel):
	# Ids
	id: PositiveInt
	# owner_id: PositiveInt
	# address_id: PositiveInt

	# Optional IDs
	tenant_id: Optional[PositiveInt] = Field(None)
	# real_estate_company_id: Optional[PositiveInt] = Field(None)

	# Enums
	type: PropertyType = Field(...)
	status: PropertyStatus = Field(...)

	# Main attributes
	name: str = Field(..., min_length=5)
	description: str = Field(..., min_length=5)
	size_m2: PositiveFloat
	listed_date: date
	last_updated: date

	# Optional values
	value: Optional[PositiveFloat] = Field(None)
	year_built: Optional[PositiveInt] = Field(None, le=datetime.today().year)


class CreatePropertySchema(PropertySchema):
	id: Optional[PositiveInt] = Field(None)
