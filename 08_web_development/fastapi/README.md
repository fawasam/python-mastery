# FastAPI Web Framework in Python

## What You Will Learn
* Modern high-performance web development with FastAPI.
* Pydantic schemas for data validation and serialization.
* Route handlers (`@app.get`, `@app.post`, `@app.put`, `@app.delete`).
* Path parameters (`/items/{item_id}`) and Query parameters (`/items?page=1`).
* Automatic OpenAPI / Swagger UI interactive documentation generation.

## Why This Matters
FastAPI is Python's leading modern web framework for building APIs. Built on Starlette and Pydantic, FastAPI offers automatic type checking, asynchronous request processing, automatic OpenAPI documentation, and industry-leading performance.

## Prerequisites
* Type Hints & Pydantic Basics (`04_intermediate_python/type_hints`)
* REST API Architecture (`08_web_development/rest_api`)

## Core Concepts

### Basic FastAPI App
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My API")

class ItemSchema(BaseModel):
    name: str
    price: float

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/items", status_code=201)
def create_item(item: ItemSchema):
    return {"created_name": item.name, "total": item.price * 1.1}
```

## Testing FastAPI with `httpx` or `TestClient`
```python
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.get("/health")
assert response.status_code == 200
```

## Exercises
See `04_exercises.py` to practice constructing FastAPI route handlers and test clients.
