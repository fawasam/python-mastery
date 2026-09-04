# Standard Library `unittest` in Python

## What You Will Learn
* Python's standard library `unittest` framework.
* `TestCase` classes and assertion methods (`assertEqual`, `assertTrue`, `assertRaises`, `assertIn`).
* Test discovery and test suites.
* `setUp()` and `tearDown()` lifecycle hooks.

## Why This Matters
`unittest` is Python's built-in xUnit-style test framework. Since it requires zero third-party dependencies, it is used extensively in enterprise software, standard library modules, and foundational open-source projects.

## Prerequisites
* Classes & Inheritance (`03_object_oriented_programming/inheritance`)
* Exceptions (`05_error_handling_debugging/exceptions`)

## Core Concepts

### `unittest.TestCase`
Tests are organized into classes inheriting from `unittest.TestCase`. Test methods must start with the `test_` prefix to be discovered by the test runner.

```python
import unittest

def add(a: int, b: int) -> int:
    return a + b

class TestMathOperations(unittest.TestCase):
    def setUp(self) -> None:
        # Runs before EVERY test method
        self.base_val = 10

    def test_add_positive_numbers((self) -> None:
        self.assertEqual(add(5, 5), 10)

    def test_add_negative_numbers(self) -> None:
        self.assertEqual(add(-5, -5), -10)

    def tearDown(self) -> None:
        # Runs after EVERY test method
        pass

if __name__ == "__main__":
    unittest.main()
```

## Common Mistakes
* **Naming test methods without `test_` prefix**: `unittest` runner ignores methods like `verify_addition()`.
* **Modifying shared state across tests**: Tests must be independent and isolated.

## Exercises
See `04_exercises.py` to practice building `unittest.TestCase` suites for a shopping cart module.
