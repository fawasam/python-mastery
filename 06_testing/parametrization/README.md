# Test Parametrization in Pytest

## What You Will Learn
* Parametrizing test functions using `@pytest.mark.parametrize`.
* Passing multiple input parameters and expected outputs.
* Stacking multiple `@pytest.mark.parametrize` decorators for matrix testing.
* Customizing test IDs for clear test reports.

## Why This Matters
Instead of writing 10 separate test functions to test different edge case inputs for the same function, parametrization executes a single test function multiple times across a dataset of test cases, reducing code duplication dramatically.

## Prerequisites
* Pytest (`06_testing/pytest`)

## Core Concepts

### `@pytest.mark.parametrize`
```python
import pytest

@pytest.mark.parametrize(
    "input_val, expected_val",
    [
        (2, 4),
        (3, 9),
        (4, 16),
        (-5, 25),
    ]
)
def test_square(input_val: int, expected_val: int):
    assert input_val ** 2 == expected_val
```

## Common Mistakes
* **Mismatch between parameter names string and test argument list**: Parameter names in `"a, b"` must match function arguments `def test_func(a, b)`.

## Exercises
See `04_exercises.py` to practice writing parametrized validation tests.
