"""
Basic SQLite Integration in Python.
"""

import sqlite3


def initialize_and_seed_database() -> None:
    # Use :memory: for temporary testing database
    conn = sqlite3.connect(":memory:")
    # Enable sqlite3.Row for column-name dictionary indexing
    conn.row_factory = sqlite3.Row

    with conn:
        conn.execute(
            """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """
        )

        # Parameterized batch insert using executemany
        sample_products = [
            ("Laptop", 1200.0),
            ("Mouse", 25.5),
            ("Keyboard", 75.0),
        ]
        conn.executemany("INSERT INTO products (name, price) VALUES (?, ?)", sample_products)

    # Query records
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products WHERE price > ?", (50.0,))
    rows = cursor.fetchall()

    print("Products with price > $50.00:")
    for row in rows:
        print(f" - ID: {row['id']} | Name: {row['name']} | Price: ${row['price']:.2f}")

    conn.close()


if __name__ == "__main__":
    initialize_and_seed_database()
