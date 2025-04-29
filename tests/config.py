import os
import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Generator
from random import randint
import pytest
from faker import Faker
from sqlalchemy.orm import Session

ROOT_PATH = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
sys.path.append(ROOT_PATH)

from db.schemas.base.base import basemodel
from db.engine import (
    MySQLConnection,
    generate_sql_connection_data,
    start_mysql_connection,
)

fake = Faker()


def database_connection():
    """Returns a testing database session running only in memory"""
    connection_data = generate_sql_connection_data(testing=True)
    sql_connection = MySQLConnection(connection_data)
    session = sql_connection.session

    # Automatically creates database tables
    basemodel.metadata.create_all(bind=sql_connection.engine)

    try:
        yield session

    finally:
        session.close()
        # Drops all tables when the connection closes
        basemodel.metadata.drop_all(bind=sql_connection.engine)


@pytest.fixture
def db_session():
    """Fixture that provides a database connection"""
    yield from database_connection()


def build_valid_tenant_data(random: bool = False) -> dict:
    if not random:
        return {
            "id": None,
            "name": "Dummy Tenant",
            "id_document": "dummy_id_document_123",
            "email": "dummy_tenant_email@tenant.com",
            "phone": "+00 (00) 0000-0000",
            "emergency_contact": "+11 (11) 1111-1111",
            "status": True,
        }

    return {
        "name": fake.name(),
        "id_document": str(datetime.now()),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "emergency_contact": fake.phone_number(),
        "status": randint(0, 1),
    }


def build_invalid_tenant_data() -> dict:
    return {
        "name": None,  # Name must not be None
        "id_document": None,  # id_document must not be None and cannot be duplicated
        "email": "invalid_mail.tenant.com",  # Email must be valid
        "status": "active",  # Status must be a boolean
    }


def remove_id(data: Any) -> Any:
    if isinstance(data, dict):
        del data["id"]
        return data

    del data.id
    return data


sql_test_connection = start_mysql_connection(testing=True)


@contextmanager
def get_test_session() -> Generator[Session, None, None]:
    """Get a database session with proper context management."""
    with sql_test_connection.session() as session:
        yield session
