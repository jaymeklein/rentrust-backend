# Rentrust Backend

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-2.11-brightgreen.svg)

A real estate management backend built with FastAPI, Pydantic, and SQLAlchemy, following MSC architecture to handle properties, tenants, owners, and leasing operations.

## 🚀 Features

- **Modern Python Stack**: FastAPI for high-performance endpoints, Pydantic for data validation, SQLAlchemy as ORM
- **Clean Architecture**: Follows MSCr pattern for maintainable and scalable code structure
- **Type Safety**: Pydantic-powered validation layer ensuring data integrity
- **Async Ready**: Async-ready design for future scalability
- **Well-Documented**: Code includes docstrings and type hints for clarity

## 📦 Project Structure
```
rentrust-backend/
├── app/ # Main application package
│ ├── config/ # API related configs
│ ├── models/ # Raw data operations (DB/API interactions)
│ ├── services/ # Core business logic & rules
│ ├── controllers/ # Data transformation/validation
│ ├── routes/ # FastAPI endpoint definitions
│ ├── schemas/ # Pydantic models/schemas
│ ├── decorators/ # Application decorators
│ ├── exceptions/ # Application exceptions
│ └── main.py # Application entry point
├── tests/ # Test suite
├── requirements.txt # Production dependencies
├── README.md # This file
```

## 🛠️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaymeklein/rentrust-backend.git
   cd rentrust-backend
   ```
2. **Set up a virtual environment (recommended)**
	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`
	```
 3. **Install dependencies**
    ```bash
    pip install pipenv# Rentrust Backend

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-2.11-brightgreen.svg)

A real estate management backend built with FastAPI, Pydantic, and SQLAlchemy, following MSC architecture to handle properties, tenants, owners, and leasing operations.

## 🚀 Features

- **Modern Python Stack**: FastAPI for high-performance endpoints, Pydantic for data validation, SQLAlchemy as ORM
- **Clean Architecture**: Follows MSCr pattern for maintainable and scalable code structure
- **Type Safety**: Pydantic-powered validation layer ensuring data integrity
- **Async Ready**: Async-ready design for future scalability
- **Well-Documented**: Code includes docstrings and type hints for clarity

## 📦 Project Structure
```
rentrust-backend/
├── app/ # Main application package
│ ├── config/ # API related configs
│ ├── models/ # Raw data operations (DB/API interactions)
│ ├── services/ # Core business logic & rules
│ ├── controllers/ # Data transformation/validation
│ ├── routes/ # FastAPI endpoint definitions
│ ├── schemas/ # Pydantic models/schemas
│ ├── decorators/ # Application decorators
│ ├── exceptions/ # Application exceptions
│ └── main.py # Application entry point
├── tests/ # Test suite
├── requirements.txt # Production dependencies
├── README.md # This file
```

## 🛠️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaymeklein/rentrust-backend.git
   cd rentrust-backend
   ```
2. **Set up a virtual environment (recommended)**
	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`
	```
 3. **Install dependencies**
    ```bash
    pip install pipenv
    pipenv install -r requirements.txt
    ```
4. **Create .env based on .env.example**
   ```bash
   cp .env .env.example
   ```
5. **Start the application (see [scripts] on Pipfile)**
	```bash
 	pipenv run dev # For development
 	pipenv run prod # For production
 	```
    pipenv install -r requirements.txt
    ```
4. **Create .env based on .env.example**
   ```bash
   cp .env .env.example
   ```
5. **Start the application (see [scripts] on Pipfile)**
	```bash
 	pipenv run dev # For development
 	pipenv run prod # For production
 	```
