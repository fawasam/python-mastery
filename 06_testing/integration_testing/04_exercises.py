"""
Integration Testing Exercises.
"""

import sqlite3


class KeyValueStore:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        with self.conn:
            self.conn.execute("CREATE TABLE kv (k TEXT PRIMARY KEY, v TEXT)")

    def set(self, key: str, val: str) -> None:
        with self.conn:
            self.conn.execute("INSERT OR REPLACE INTO kv (k, v) VALUES (?, ?)", (key, val))

    def get(self, key: str) -> str | None:
        cur = self.conn.execute("SELECT v FROM kv WHERE k = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else None


# Exercise 1 (Medium): Write an integration test function for KeyValueStore
def test_key_value_store_integration() -> None:
    raise NotImplementedError("Implement test_key_value_store_integration with SQLite :memory:")
