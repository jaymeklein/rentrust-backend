from functools import wraps

from sqlalchemy.orm import Session

from db.engine import get_engine


def with_session(func):
	"""Decorator to inject a session within a class method."""

	@wraps(func)
	def wrapper(cls, *args, **kwargs):
		with Session(get_engine()) as session:
			return func(cls, session, *args, **kwargs)

	return wrapper
