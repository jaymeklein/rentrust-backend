class Base(Exception):
	""" Common base class for all non-exit exceptions. """
	pass


class DatabaseException(Base):
	""" Common base class for all exceptions raised by database. """


class DataValidationException(Base):
	""" Common base class for all exceptions raised by data validation. """


class DatabaseDataValidationException(DataValidationException):
	""" Common base class for all exceptions raised by database data validation. """
	pass
