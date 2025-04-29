from typing import Optional

from pydantic import BaseModel, PositiveInt


class SqlConnectionData(BaseModel):
    user: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[PositiveInt | str] = None
    database: Optional[str] = None
    is_sqlite: bool = False
    url: Optional[str] = None
