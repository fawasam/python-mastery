# API Documentation & OpenAPI Specification in Python

## What You Will Learn
* OpenAPI 3.0 specification & Swagger UI / ReDoc generation.
* Enhancing route documentation using docstrings, `summary`, `description`, and `response_description`.
* Documenting path/query parameter metadata with `Field` and `Query`.
* Schema definitions with Pydantic model `json_schema_extra` / `Field(description=...)`.

## Why This Matters
Clear, up-to-date API documentation allows frontend developers, mobile teams, and API consumers to integrate with your web services effortlessly. Frameworks like FastAPI auto-generate interactive Swagger UI `/docs` endpoints directly from your code annotations and docstrings.

## Prerequisites
* FastAPI (`08_web_development/fastapi`)
* Pydantic (`04_intermediate_python/type_hints`)

## Core Concepts

### Documenting FastAPI Endpoints
```python
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Inventory API", version="1.0.0")

class ItemCreate(BaseModel):
    name: str = Field(..., description="Unique product SKU name", example="Mechanical Keyboard")
    price: float = Field(..., gt=0.0, description="Unit price in USD", example=99.99)

@app.post("/items", summary="Create a new inventory item", response_description="The created item with ID")
def create_item(item: ItemCreate):
    """
    Creates a new product item in the inventory catalog.
    - **name**: Must be non-empty string.
    - **price**: Must be strictly positive number.
    """
    return {"id": 1, "name": item.name, "price": item.price}
```

## Exercises
See `04_exercises.py` to practice building documented Pydantic schemas and OpenAPI metadata.
