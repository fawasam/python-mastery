# Test-Driven Development (TDD) in Python

## What You Will Learn
* The TDD Red-Green-Refactor cycle.
* Writing failing unit tests before writing production code.
* Implementing minimal code to make failing tests pass (Green).
* Refactoring production code cleanly under test coverage protection.

## Why This Matters
TDD forces clean software architecture, modular decoupling, and continuous regression testing. Writing tests first prevents over-engineering and clarifies business requirements before writing implementation code.

## Prerequisites
* Pytest (`06_testing/pytest`)

## Core Concepts

### The Red-Green-Refactor Cycle
1. **RED**: Write a failing test for a feature that does not exist yet. Verify the test fails for the expected reason.
2. **GREEN**: Write the minimal amount of production code required to make the failing test pass.
3. **REFACTOR**: Clean up duplicate code and improve design while ensuring all tests continue to pass.

```text
    Write Failing Test (RED)
             │
             ▼
    Make Test Pass (GREEN)
             │
             ▼
    Refactor Code (REFACTOR)
```

## Exercises
See `04_exercises.py` to practice TDD implementation of a Roman Numeral Converter module.
