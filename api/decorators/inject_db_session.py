from functools import wraps

from db.engine import get_session


def with_session(func, testing: bool = False):
	"""Decorator to inject a database session within a class method."""

	@wraps(func)
	def wrapper(cls, *args, **kwargs):
		with get_session(testing) as session:
			return func(cls, session, *args, **kwargs)

	return wrapper
