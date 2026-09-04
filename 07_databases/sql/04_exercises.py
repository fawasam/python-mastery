"""
SQL Query Exercises.
"""

import sqlite3


# Exercise 1 (Medium): High Earner Count Query
# Write get_high_earners_count(conn: sqlite3.Connection, min_salary: float) -> int
# Executes SELECT COUNT(*) FROM employees WHERE salary >= min_salary and returns result integer.
def get_high_earners_count(conn: sqlite3.Connection, min_salary: float) -> int:
    raise NotImplementedError("Implement get_high_earners_count")
