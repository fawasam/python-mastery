# Web API Middleware in Python

## What You Will Learn
* The Middleware pattern in WSGI & ASGI web frameworks.
* Intercepting request and response cycles.
* Adding request processing timing headers (`X-Process-Time`).
* Request rate limiting and CORS middleware.

## Why This Matters
Middleware acts as a pipeline wrapper around all incoming HTTP requests and outgoing HTTP responses. It lets you add cross-cutting concerns (logging, timing, CORS headers, error boundary catching, authentication token extraction) centrally without cluttering individual route handler functions.

## Prerequisites
* Decorators & Functions (`02_core_python/decorators`, `04_intermediate_python/advanced_decorators`)
* FastAPI / Starlette (`08_web_development/fastapi`)

## Core Concepts

### FastAPI / Starlette Middleware
```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    return response
```

## Exercises
See `04_exercises.py` to practice building timing and custom header middlewares.
