# Project 11: Production-Grade Enterprise FastAPI Service Architecture

## Overview
A complete enterprise FastAPI backend service implementing Clean Architecture layering (API -> Service -> Repository -> Models/Schemas).

## Architecture Breakdown

```text
11_production_fastapi_application/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/             # HTTP Routing controllers
│   ├── services/        # Business use-case logic
│   ├── models/          # ORM database entities
│   ├── schemas/         # Pydantic data validation schemas
│   ├── repositories/    # Database data access abstraction
│   ├── core/            # App configuration & security settings
│   └── utils/           # Utility functions
│
├── tests/               # Pytest integration tests
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Why Each Layer Exists
1. **`api/`**: Exposes HTTP routes and validates incoming payloads.
2. **`services/`**: Encapsulates business logic, decoupled from HTTP frameworks and databases.
3. **`repositories/`**: Handles database interactions (SQLAlchemy/SQLite) using the Repository Pattern.
4. **`models/`**: Defines SQLAlchemy ORM database table schemas.
5. **`schemas/`**: Defines Pydantic data contracts for request/response serialization.
6. **`core/`**: Centralizes application settings and environment variables.

## Running with Docker
```bash
docker-compose up --build
```
