from api.exceptions.base_exceptions import DatabaseDataValidationException


class TenantAlreadyExistsException(DatabaseDataValidationException):
	""" Common base class for when a tenant already exists and someone tried to create it. """
	pass

class TenantNotFoundException(DatabaseDataValidationException):
	""" Common base class for when a tenant does not exist. """
	pass
