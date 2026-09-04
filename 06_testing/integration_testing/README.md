# Integration Testing in Python

## What You Will Learn
* Differences between Unit Tests and Integration Tests.
* Testing multiple combined components (Repository + Database / Service + Cache).
* Managing real vs in-memory test databases (e.g. SQLite `:memory:`).
* Cleanup strategies to ensure clean test state across integration runs.

## Why This Matters
While unit tests test individual functions in isolation, integration tests verify that all system components (ORM, database queries, file storage, network adapters) work together correctly in harmony.

## Prerequisites
* Pytest & Fixtures (`06_testing/pytest`, `06_testing/fixtures`)

## Core Concepts

### Unit vs Integration Testing
- **Unit Test**: Mocks database and network calls. Executes in milliseconds.
- **Integration Test**: Uses actual (or in-memory) database/file storage to test actual query execution and multi-layer interaction.

```python
# Integration Test using SQLite in-memory database
def test_user_repository_integration():
    db = create_in_memory_sqlite_db()
    repo = UserRepository(db)
    user = repo.save(User("alice"))
    assert repo.find_by_id(user.id).username == "alice"
```

## Common Mistakes
* **Not cleaning up database state between integration tests**: Test A leaves records in the database, causing Test B to fail randomly (order-dependent test failures).

## Exercises
See `04_exercises.py` to practice building in-memory SQLite integration tests.
