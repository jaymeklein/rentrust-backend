from contextlib import contextmanager
from os import getenv
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, Engine
from sqlalchemy.orm import sessionmaker, Session

from db.models import SqlConnectionData
from db.schemas.base.base import basemodel
from db.tables import *

load_dotenv()


class MySQLConnection:
	def __init__(self, connection_data: SqlConnectionData):
		self.host = connection_data.host
		self.port = connection_data.port
		self.user = connection_data.user
		self.password = connection_data.password
		self.database = connection_data.database
		self.is_sqlite = connection_data.is_sqlite
		self.url = connection_data.url

		if not all([self.user, self.port, self.host, self.password, self.database]) and not self.is_sqlite:
			raise ValueError("Missing SQL connection parameter(s)")

		self._engine = create_engine(
			self.url if self.is_sqlite else URL.create(
				"mysql",
				username=self.user,
				password=self.password,
				host=self.host,
				database=self.database,
				port=self.port,
			),
			echo=False,
			future=True
		)

		basemodel.metadata.create_all(self._engine)
		self._session_factory = sessionmaker(
			bind=self._engine,
			future=True,
			expire_on_commit=False
		)

	@contextmanager
	def session(self) -> Generator[Session, None, None]:
		"""Provide a transactional scope around a series of operations."""
		session = self._session_factory()
		try:
			yield session
			session.commit()
		except Exception:
			session.rollback()
			raise
		finally:
			session.close()

	@property
	def engine(self) -> Engine:
		return self._engine


def generate_sql_connection_data(testing: bool = False) -> SqlConnectionData:
	db_url = getenv("PRIVATE_DB_URL")
	if testing:
		db_url = getenv("PRIVATE_TEST_DB_URL")

	return SqlConnectionData(
		user=getenv("PRIVATE_DB_USER"),
		password=getenv("PRIVATE_DB_PASSWORD"),
		host=getenv("PRIVATE_DB_HOST"),
		port=getenv("PRIVATE_DB_PORT"),
		database=getenv("PRIVATE_MYSQL_DATABASE"),
		is_sqlite=bool(getenv("USE_SQLITE")),
		url=db_url,
	)


def start_mysql_connection(testing: bool = False) -> MySQLConnection:
	connection_data = generate_sql_connection_data(testing)
	return MySQLConnection(connection_data)


# Initialize connections
sql_connection = start_mysql_connection()


@contextmanager
def get_session() -> Generator[Session, None, None]:
	"""Get a database session with proper context management."""
	with sql_connection.session() as session:
		yield session
