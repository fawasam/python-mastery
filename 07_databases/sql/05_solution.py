"""
Solutions for SQL Exercises.
"""

import sqlite3


def get_high_earners_count(conn: sqlite3.Connection, min_salary: float) -> int:
    cursor = conn.execute("SELECT COUNT(*) FROM employees WHERE salary >= ?", (min_salary,))
    return cursor.fetchone()[0]


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, salary REAL)")
        conn.executemany("INSERT INTO employees (salary) VALUES (?)", [(50000.0,), (80000.0,), (120000.0,)])

    count = get_high_earners_count(conn, 75000.0)
    assert count == 2
    print(f"High earners count (>= $75,000): {count}")
    conn.close()
