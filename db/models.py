from typing import Optional

from pydantic import BaseModel, PositiveInt


class SqlConnectionData(BaseModel):
	user: str
	password: str
	host: str
	port: PositiveInt
	database: Optional[str] = None
	is_sqlite: bool = False
	url: Optional[str] = None
