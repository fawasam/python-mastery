"""
Solutions for SQLite Exercises.
"""

import sqlite3


def create_employee_db(conn: sqlite3.Connection) -> None:
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """
        )
        conn.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("Alice", "Engineering", 95000.0))
        conn.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("Bob", "Marketing", 75000.0))


if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    create_employee_db(connection)

    cur = connection.execute("SELECT COUNT(*) FROM employees")
    count = cur.fetchone()[0]
    assert count == 2
    print(f"Employee database created with {count} records successfully!")
    connection.close()
