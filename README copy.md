# Automatically generate tables

1. Inside `/rentrust`, generate the version file:
    ```bash
    alembic revision --autogenerate -m "MESSAGE"
    ```
2. Push changes to the database
    ```bash
    alembic upgrade head
    ```
