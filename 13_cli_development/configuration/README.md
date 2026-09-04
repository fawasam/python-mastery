# Application Configuration Management in Python

## What You Will Learn
- Precedence order in configuration: CLI flags > Environment Variables > Config File (`.env` / `config.json` / `pyproject.toml`) > Defaults
- Reading environment variables safely using `os.getenv()` and `pydantic-settings`
- Parsing JSON, YAML, and TOML config files
- Building type-safe configuration dataclass models

## Why This Matters
CLI tools and microservices must adapt dynamically across development, staging, and production environments without code modification (12-Factor App methodology).

## Precedence Hierarchy

```text
 (Highest Priority)
   1. CLI Arguments (--db-port 5433)
   2. Environment Variables (DB_PORT=5433)
   3. Configuration File (.env / config.json)
   4. Application Default Values (DB_PORT=5432)
 (Lowest Priority)
```

## Examples
See `01_basic.py` (JSON/Env loading) and `02_examples.py` (Pydantic Settings precedence).

## Exercises
Complete exercises in `04_exercises.py` and verify in `05_solution.py`.

## Next Topic
Complete the CLI Development Mini Project in `../mini_project/`.
