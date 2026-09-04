# SQLAlchemy 2.0 Core & Expression Language in Python

## What You Will Learn
* Modern SQLAlchemy 2.0 `create_engine()` and `MetaData`.
* Declaring tables using `Table`, `Column`, `Integer`, `String`.
* Executing SQL expressions with `select()`, `insert()`, `update()`, `delete()`.
* Connection context management with `with engine.connect() as conn:`.

## Why This Matters
SQLAlchemy is the premier database toolkit in Python. Understanding SQLAlchemy Core provides database independence, type-safe query construction, and automatic SQL dialect translation across PostgreSQL, SQLite, MySQL, and Oracle.

## Prerequisites
* Relational SQL (`07_databases/sql`)

## Core Concepts

### SQLAlchemy 2.0 Engine & Selection
```python
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
)

metadata.create_all(engine)

# Modern 2.0 select query
stmt = select(users_table).where(users_table.c.username == "alice")
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row)
```

## Common Mistakes
* **Using legacy 1.x `engine.execute()` style**: SQLAlchemy 2.0 requires using `conn.execute()` within an active connection block.
* **Forgetting `conn.commit()` when making modifications outside auto-commit blocks**: Use `with engine.begin() as conn:` to auto-commit DML statements.

## Exercises
See `04_exercises.py` to practice constructing SQLAlchemy Core select and filter statements.
