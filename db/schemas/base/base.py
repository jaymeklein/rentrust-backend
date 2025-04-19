from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

base = declarative_base(metadata=MetaData())
base.__table_args__ = {'extend_existing': True}


class BaseModel(base):
	__abstract__ = True

	def as_dict(self, exclude: list[str] = None) -> dict:
		"""Convert model instance to a dictionary, excluding SQLAlchemy internals."""
		if exclude is None:
			exclude = ["registry", "metadata", "query", "query_class"]

		return {
			key: getattr(self, key)
			for key in self.__mapper__.c.keys()  # Only column attributes
			if key not in exclude
		}

basemodel = BaseModel
