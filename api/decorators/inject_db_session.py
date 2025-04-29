from functools import wraps
from typing import Callable

from db.engine import get_session
from tests.config import get_test_session


def with_session(func) -> Callable:
    """Decorator to inject a database session within a class method."""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        testing = getattr(self, "testing", False)
        if testing:
            with get_test_session() as session:
                return func(self, session, *args, **kwargs)

        with get_session() as session:
            return func(self, session, *args, **kwargs)

    return wrapper
