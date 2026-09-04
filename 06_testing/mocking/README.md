# Mocking in Python (`unittest.mock`)

## What You Will Learn
* Python's built-in `unittest.mock` library.
* `Mock` and `MagicMock` objects.
* Patching external dependencies with `@patch` and `patch.object`.
* Asserting call history (`assert_called_once_with`, `assert_called_with`).
* Configuring `return_value` vs `side_effect`.

## Why This Matters
Unit tests should run fast and deterministically without making actual HTTP requests, sending emails, or querying production databases. Mocking replaces external dependencies with controllable dummy objects.

## Prerequisites
* Decorators (`02_core_python/decorators`)
* Pytest (`06_testing/pytest`)

## Core Concepts

### 1. `MagicMock` and `Mock`
A `Mock` object creates attributes and method calls dynamically on-the-fly and records all invocations.

```python
from unittest.mock import MagicMock

mock_client = MagicMock()
mock_client.fetch_user.return_value = {"id": 1, "name": "Alice"}

result = mock_client.fetch_user(1)
mock_client.fetch_user.assert_called_once_with(1)
```

### 2. Patching Target Path Rule
Always patch where the object is **LOOKED UP** (imported), NOT where it is defined!

```python
# Bad: @patch("requests.get")
# Good (if app.py imports requests): @patch("app.requests.get")
```

## Common Mistakes
* **Incorrect patch target path**: Patching the source module instead of the importing target module leads to un-mocked actual network calls!
* **Over-mocking**: Mocking everything including core domain entities defeats the purpose of unit testing logic.

## Exercises
See `04_exercises.py` to practice mocking REST API network requests and file system reads.
