# API Authorization & Role-Based Access Control (RBAC) in Python

## What You Will Learn
* Authentication (Who are you?) vs Authorization (What are you allowed to do?).
* Role-Based Access Control (RBAC: `admin`, `editor`, `viewer`).
* Attribute-Based Access Control (ABAC: resource ownership checks).
* Implementing authorization decorators and dependencies in FastAPI.

## Why This Matters
Authentication verifies identity, but authorization ensures users only access resources they own or have permission to manage. Without proper authorization checks, regular users could read or delete administrative data (BOLA / IDOR vulnerabilities).

## Prerequisites
* Authentication (`08_web_development/authentication`)
* FastAPI (`08_web_development/fastapi`)

## Core Concepts

### Role-Based Access Control (RBAC) Pattern
```python
from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

def require_role(required_role: Role):
    def dependency(user_role: Role):
        if user_role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden: Higher privilege required")
    return dependency
```

## Exercises
See `04_exercises.py` to practice building role-checking authorization functions.
