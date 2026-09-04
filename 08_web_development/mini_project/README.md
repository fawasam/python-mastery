# Mini Project: Production-Grade Task Management REST Microservice

## Overview
This mini project combines key web development concepts into a complete FastAPI REST API:
1. **REST Architecture**: Clean HTTP verbs and resource routing (`/api/v1/tasks`).
2. **API Authentication**: Header-based `X-API-Key` dependency security.
3. **Middleware**: Response time tracking (`X-Process-Time-MS`).
4. **Interactive OpenAPI Specs**: Full Swagger UI documentation metadata.

## How to Run
Run tests directly using Python:
```bash
python main.py
```
Or start dev server with Uvicorn:
```bash
uvicorn main:app --reload
```
View interactive documentation at `http://127.0.0.1:8000/docs`.
