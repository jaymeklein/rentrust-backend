from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel as PydanticBaseModel

base = declarative_base(metadata=MetaData())
base.__table_args__ = {"extend_existing": True}


class BaseModel(base):
    __abstract__ = True

    def as_dict(self, exclude: list[str] | None = None) -> dict:
        """Convert model instance to a dictionary, excluding SQLAlchemy internals."""
        if exclude is None:
            exclude = ["registry", "metadata", "query", "query_class"]

        return {
            key: getattr(self, key)
            for key in self.__mapper__.c.keys()  # Only column attributes
            if key not in exclude
        }

    def _validate_ignored_keys(
        self, ignored_keys: list[str] | None = None
    ) -> list[str]:
        """Validate ignored keys."""
        if ignored_keys is None:
            ignored_keys = []

        must_ignore_keys = ["id"]
        for key in must_ignore_keys:
            if key not in ignored_keys:
                ignored_keys.append(key)

        return ignored_keys

    def update_from_dict(
        self, data: dict, ignored_keys: list[str] | None = None
    ) -> None:
        """Update model instance from a dictionary."""
        ignored_keys = self._validate_ignored_keys(ignored_keys)

        for key, value in data.items():
            if key in ignored_keys:
                continue

            setattr(self, key, value)

    def update_from_model(
        self, model: PydanticBaseModel, ignored_keys: list[str] | None = None
    ) -> None:
        """Update SQLAlchemy model instance from Pydantic model instance."""
        self.update_from_dict(model.model_dump(), ignored_keys=ignored_keys)


basemodel = BaseModel
