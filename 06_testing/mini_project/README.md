# Mini Project: Automated Test Suite & Financial Engine

## Overview
This mini project demonstrates a complete production-grade testing suite for a financial transaction service.

It incorporates:
1. **Fixtures & In-Memory Databases**: Fast integration testing with SQLite in-memory connections.
2. **Mocking**: Isolated unit tests mocking external Currency Exchange Rate API adapters.
3. **Parametrization**: Multi-input fee evaluation tests.
4. **Exception Assertions**: Ensuring validation failures raise clean, typed domain exceptions.

## How to Run
Run tests directly using Python or pytest:
```bash
python main.py
# Or using pytest:
pytest main.py
```
