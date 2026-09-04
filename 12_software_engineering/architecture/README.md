# Clean Architecture and Layering in Python

## What You Will Learn
- Clean Architecture principles (Onion / Hexagonal Architecture)
- The Repository Pattern for database abstraction
- The Service Layer for business logic encapsulation
- Separation of Concerns: Entities vs Use Cases vs Interfaces

## Why This Matters
Mixing database queries, business rules, and HTTP presentation logic into single functions makes applications unmaintainable. Layered clean architecture isolates core domain logic from external frameworks, databases, and UI implementations.

## Layer Breakdown

```text
       [ Presentation Layer (FastAPI / CLI / Flask) ]
                         ↓
       [ Application / Service Layer (Use Cases) ]
                         ↓
       [ Domain Layer (Entities & Business Rules) ]
                         ↑
       [ Infrastructure Layer (Repositories, DB, APIs) ]
```

## Core Patterns

### 1. Repository Pattern
Abstracts data access logic behind an interface so business logic never executes raw SQL or database queries directly.

### 2. Service Layer
Encapsulates application use-case logic and coordinates domain entities with repositories.

## Examples
See `01_basic.py` for a complete runnable implementation of the Repository Pattern & Service Layer.

## Exercises
Complete exercises in `04_exercises.py` and verify solutions in `05_solution.py`.

## Next Topic
Proceed to `../modular_design/`.
