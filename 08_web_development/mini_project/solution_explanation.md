# Solution Explanation: Task Management REST Microservice

## System Design Highlights

1. **FastAPI & Pydantic Validation (`TaskCreateSchema`, `TaskResponseSchema`)**:
   Enforces payload types, non-empty titles, and auto-generates OpenAPI 3.0 documentation.

2. **Security & Dependency Injection (`Depends(verify_api_key)`)**:
   Mandates the `X-API-Key` request header across all task mutation and query endpoints. Unauthenticated requests are rejected immediately with 401 Unauthorized before route handler execution.

3. **HTTP Middleware (`process_time_middleware`)**:
   Wraps every request and injects latency metrics into `X-Process-Time-MS` response headers.
