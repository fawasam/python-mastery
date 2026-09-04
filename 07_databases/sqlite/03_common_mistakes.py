"""
Common Mistakes in SQLite Integration.
"""

import sqlite3


# MISTAKE 1: SQL Injection via f-strings
def mistake_sql_injection(conn: sqlite3.Connection, user_input: str) -> None:
    # DANGER: If user_input is "' OR '1'='1", this executes SELECT * FROM users WHERE name = '' OR '1'='1'!
    # Exposes all records in the database!
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    # DANGEROUS SECURITY VULNERABILITY!
    pass


# GOOD PRACTICE: Parameterized SQL placeholders
def good_parameterized_query(conn: sqlite3.Connection, user_input: str) -> None:
    conn.execute("SELECT * FROM users WHERE name = ?", (user_input,))


if __name__ == "__main__":
    print("Always use parameterized queries '?' placeholders to prevent SQL Injection!")
