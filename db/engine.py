from os import getenv
from typing import Any, Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, Engine
from sqlalchemy.orm import sessionmaker, Session

from db.models import SqlConnectionData

load_dotenv()


class MySQLConnection:
	__session: Session = None
	__engine: Engine = None

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

		if self.__session is None:
			self.create_session()

	def create_session(self) -> None:

		url_obj = self.url
		if not self.is_sqlite:
			url_obj = URL.create(
				"mysql",
				username=self.user,
				password=self.password,
				host=self.host,
				database=self.database,
				port=self.port,
			)

		self.__engine = create_engine(url_obj, echo=False, future=True)
		session = sessionmaker(bind=self.__engine, future=True)
		self.__session = session()

	@property
	def get_session(self) -> Session:
		return self.__session

	@property
	def get_engine(self) -> Engine:
		return self.__engine


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


def start_mysql_connection(testing: bool = False) -> Session:
	connection_data = generate_sql_connection_data(testing)
	sql_connection = MySQLConnection(connection_data)
	return sql_connection.get_session


sql_session = start_mysql_connection()
sql_test_session = start_mysql_connection(testing=True)


def get_session(testing: bool = False) -> Generator[Session, Any, None]:
	database = sql_session
	if testing:
		database = sql_test_session

	try:
		yield database
	finally:
		database.close()
