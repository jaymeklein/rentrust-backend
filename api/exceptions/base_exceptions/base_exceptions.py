
class Base(Exception):
	""" Common base class for all non-exit exceptions. """
	pass

class DataValidationException(Base):
	""" Common base class for all exceptions raised by data validation. """
	pass

class DatabaseDataValidationException(DataValidationException):
	""" Common base class for all exceptions raised by database data validation. """
	pass
