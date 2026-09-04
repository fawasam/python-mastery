# Pytest Fixtures in Python

## What You Will Learn
* Defining fixtures with `@pytest.fixture`.
* Dependency injection in pytest (requesting fixtures by argument name).
* Fixture scopes (`function`, `class`, `module`, `session`).
* Resource setup and teardown using yield fixtures (`yield`).
* `conftest.py` for sharing fixtures across test directories.

## Why This Matters
Fixtures provide a reliable, modular, and reusable setup mechanism for test data, database connections, mock clients, and temporary directories. Using fixtures eliminates boilerplate setup code in your test suite.

## Prerequisites
* Pytest (`06_testing/pytest`)
* Generators (`02_core_python/generators`)

## Core Concepts

### Yield Fixture Pattern
```python
import pytest

@pytest.fixture
def db_connection():
    # Setup phase
    conn = connect_test_db()
    yield conn  # Hand control to test function
    # Teardown phase (runs after test completes!)
    conn.close()
```

## Common Mistakes
* **Mutating fixture data across tests without copying**: Returning mutable objects (e.g. `list`, `dict`) from higher-scoped fixtures (`module`, `session`) can cause test pollution when tests alter fixture contents.

## Exercises
See `04_exercises.py` to practice writing setup/teardown yield fixtures.
