"""
SQL INNER JOIN and LEFT JOIN Relational Queries.
"""

import sqlite3


def demo_sql_joins() -> None:
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT)")

        conn.executemany("INSERT INTO users VALUES (?, ?)", [(1, "Alice"), (2, "Bob"), (3, "Charlie")])
        conn.executemany("INSERT INTO orders VALUES (?, ?, ?)", [(101, 1, "Laptop"), (102, 1, "Mouse"), (103, 2, "Keyboard")])

    # INNER JOIN: Returns only users who have placed orders
    print("--- INNER JOIN Results ---")
    inner_query = """
        SELECT users.name, orders.item
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
    """
    for name, item in conn.execute(inner_query):
        print(f" {name} ordered {item}")

    # LEFT JOIN: Returns ALL users including Charlie who has 0 orders
    print("\n--- LEFT JOIN Results ---")
    left_query = """
        SELECT users.name, orders.item
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
    """
    for name, item in conn.execute(left_query):
        print(f" {name} ordered {item or 'Nothing'}")

    conn.close()


if __name__ == "__main__":
    demo_sql_joins()
