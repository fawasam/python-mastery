# Pytest in Python

## What You Will Learn
* Modern testing using `pytest`.
* Plain `assert` statements vs verbose `unittest` assertion methods.
* Testing exception raising with `pytest.raises()`.
* Running tests via `pytest` CLI runner.
* Test organization and conventions.

## Why This Matters
`pytest` is the industry standard test framework in Python. It offers clean, readable syntax using native `assert` statements, powerful introspection output on failures, auto-discovery, and an ecosystem of plugins (coverage, async, mocking).

## Prerequisites
* Standard Unittest (`06_testing/unittest`)

## Core Concepts

### 1. Plain Assert Statements
Unlike `unittest`, `pytest` automatically intercepts standard Python `assert` statements and rewrites them to provide rich contextual diffs when tests fail.

```python
def test_string_formatting():
    name = "alice"
    assert name.upper() == "ALICE"
```

### 2. Exception Testing with `pytest.raises`
```python
import pytest

def test_divide_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        _ = 1 / 0
    assert "division by zero" in str(exc_info.value)
```

## Common Mistakes
* **Using `unittest` methods in plain pytest functions**: Writing `self.assertEqual()` outside a `unittest.TestCase` class raises `NameError`.
* **Not installing pytest in virtual environment**: `pytest` requires installation (`pip install pytest`).

## Exercises
See `04_exercises.py` to practice converting legacy unittest functions into modern pytest functions.
