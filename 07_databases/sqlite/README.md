# SQLite Database Integration in Python

## What You Will Learn
* Python's standard library `sqlite3` module.
* Creating database connections and cursors.
* Executing SQL DDL (`CREATE TABLE`) and DML (`INSERT`, `SELECT`, `UPDATE`, `DELETE`).
* Parameterized queries to prevent SQL Injection (`?` placeholders).
* Row factories for dict-like row access (`sqlite3.Row`).

## Why This Matters
SQLite is a zero-configuration, file-based SQL database engine built directly into Python. It is ideal for local development, desktop applications, embedded systems, and unit testing database layers.

## Prerequisites
* Basic File Handling (`01_beginner/17_basic_file_handling`)
* Exception Handling (`05_error_handling_debugging/exceptions`)

## Core Concepts

### Parameterized Queries (Preventing SQL Injection)
NEVER use f-strings or string concatenation to insert variables into SQL statements! Always use parameterized placeholders:

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# GOOD: Safe parameterized query
cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))
```

### Context Managers for Transactions
Using `with conn:` automatically commits transactions on success or rolls back if an exception occurs:

```python
with conn:
    conn.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
```

## Common Mistakes
* **String formatting in SQL queries**: `cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")` creates critical SQL Injection vulnerabilities!
* **Forgetting to commit transactions**: Data inserted without calling `conn.commit()` or `with conn:` will be lost when connection closes.

## Exercises
See `04_exercises.py` to practice creating a parameterized user inventory database.
