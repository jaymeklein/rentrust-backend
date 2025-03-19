import os

import pytest
from sqlalchemy.orm import sessionmaker

from db.engine import generate_engine
from db.schemas.base.base import Base

DATABASE_URL = os.environ.get("PRIVATE_TEST_DATABASE_URL")
PRODUCTION = False


@pytest.fixture
def database_connection():
	engine = generate_engine(DATABASE_URL, PRODUCTION)
	local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
	Base.metadata.create_all(bind=engine)
	db = local_session()

	try:
		yield db

	finally:
		db.close()
		Base.metadata.drop_all(bind=engine)
