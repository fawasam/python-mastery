# HTTP Client Requests (`httpx` / `requests`) in Python

## What You Will Learn
* Making synchronous HTTP requests with `httpx` / `requests`.
* Sending `GET`, `POST`, `PUT`, `DELETE` requests.
* Passing query parameters (`params`), JSON payloads (`json`), and custom headers (`headers`).
* Handling response status checks (`response.raise_for_status()`).
* Setting request timeouts and retry parameters.

## Why This Matters
Consuming third-party web APIs, microservices, and external OAuth servers requires an HTTP client library. `httpx` provides a modern, type-safe API compatible with standard `requests` syntax while supporting both sync and async operations.

## Prerequisites
* HTTP Fundamentals (`08_web_development/http`)
* JSON (`02_core_python/json`)

## Core Concepts

### Making Requests with `httpx`
```python
import httpx

# Synchronous GET request
response = httpx.get("https://api.github.com/events", timeout=5.0)
response.raise_for_status()  # Raises HTTPStatusError if 4xx/5xx
data = response.json()
```

## Common Mistakes
* **Making requests without a timeout**: Leaving `timeout=None` allows network stalls to hang your application threads indefinitely!
* **Not checking response status**: Assuming every request returns `200 OK` causes crash failures when servers return `404` or `500`.

## Exercises
See `04_exercises.py` to practice creating API client wrappers with status handling.
