from api.exceptions.base_exceptions import (
    DatabaseDataValidationException,
    DataValidationException,
)


class PropertyNotFoundException(DatabaseDataValidationException):
    """Common base class for when a property does not exist."""


class MissingUpdateFieldException(DataValidationException):
    """Common base class for when a property does not exist."""
