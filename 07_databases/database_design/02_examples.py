"""
Database Indexing for Query Optimization.
"""

import sqlite3
import time


def demo_indexing_performance() -> None:
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
        # Insert 10,000 records
        conn.executemany("INSERT INTO users (email) VALUES (?)", [(f"user_{i}@example.com",) for i in range(10_000)])

    # Search BEFORE index
    t0 = time.perf_counter()
    _ = conn.execute("SELECT * FROM users WHERE email = 'user_9999@example.com'").fetchall()
    t_no_index = time.perf_counter() - t0

    # Create Index on email column
    with conn:
        conn.execute("CREATE INDEX idx_users_email ON users(email)")

    # Search AFTER index
    t1 = time.perf_counter()
    _ = conn.execute("SELECT * FROM users WHERE email = 'user_9999@example.com'").fetchall()
    t_indexed = time.perf_counter() - t1

    print(f"Query duration WITHOUT Index: {t_no_index * 1000:.4f} ms")
    print(f"Query duration WITH Index   : {t_indexed * 1000:.4f} ms")
    conn.close()


if __name__ == "__main__":
    demo_indexing_performance()
