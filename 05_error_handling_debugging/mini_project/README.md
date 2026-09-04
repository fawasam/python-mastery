# Mini Project: Resilient Data Ingestion & Fault Telemetry Engine

## Overview
This mini project brings together the core components of error handling and debugging:
1. **Custom Exception Hierarchies**: Standardized domain exceptions (`IngestionError`, `ParseError`, `ConnectionError`).
2. **Exception Chaining**: Wrapping low-level socket/JSON errors into business domain exceptions with `from err`.
3. **Structured Logging**: Configured stream logging with error context formatting.
4. **Defensive Programming**: Fail-fast guard clause validation and defensive object copying.

## Running the Project
```bash
python main.py
```
