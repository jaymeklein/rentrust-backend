import os
import sys
from pathlib import Path

import pytest

ROOT_PATH = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
sys.path.append(ROOT_PATH)

from db.engine import MySQLConnection, generate_sql_connection_data
from db.schemas.base.base import Base



def database_connection():
	"""Returns a testing database session running only in memory"""
	connection_data = generate_sql_connection_data(testing=True)
	sql_connection = MySQLConnection(connection_data)
	session = sql_connection.get_session

	# Automatically creates database tables
	Base.metadata.create_all(bind=sql_connection.get_engine)

	try:
		yield session

	finally:
		session.close()
		# Drops all tables when the connection closes
		Base.metadata.drop_all(bind=sql_connection.get_engine)

@pytest.fixture
def db_session():
	"""Fixture that provides a database connection"""
	yield from database_connection()
