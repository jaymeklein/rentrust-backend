# Structure
	Router (routes) - Maps endpoints to controller methods;
	Controller (controllers) - Manages request/response flow and delegates to the service;
	Service (services) - Handles business logic and data operations;
	Model (models) - Interacts with the database;
 	Schema (schemas) - Defines Pydantic types;
   	Schema (db/schemas) - Defines the data structure as SQLAlchemy models;

# Dynamically generate database tables
	1. Inside `/rentrust`, generate the version file:
	   ```bash
	   alembic revision --autogenerate -m "MESSAGE"
	   ```
	2. Push changes to the database
	   ```bash
	   alembic upgrade head
	   ```
