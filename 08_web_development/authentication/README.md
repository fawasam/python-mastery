# API Authentication Patterns in Python

## What You Will Learn
* Authentication vs Authorization.
* Password Hashing (PBKDF2, bcrypt, SHA-256 with Salt).
* API Key Authentication via HTTP Headers (`X-API-Key`).
* JSON Web Token (JWT) concepts & Bearer Token authentication.
* Session / Token management.

## Why This Matters
Exposing unprotected web APIs allows unauthorized users to tamper with or steal sensitive user data. Implementing strong password hashing and token-based authentication protects backend endpoints from unauthorized access.

## Prerequisites
* HTTP & FastAPI (`08_web_development/http`, `08_web_development/fastapi`)

## Core Concepts

### Password Hashing (Salt + PBKDF2 / SHA256)
NEVER store plain-text passwords in databases! Always hash passwords using a secure key derivation function with a unique per-user salt.

```python
import hashlib
import os

def hash_password(password: str) -> tuple[bytes, str]:
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt, hashed.hex()
```

## Exercises
See `04_exercises.py` to practice implementing password hashing and verification.
