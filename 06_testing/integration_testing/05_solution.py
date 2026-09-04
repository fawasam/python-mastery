"""
Solutions for Integration Testing Exercises.
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


def test_key_value_store_integration() -> None:
    conn = sqlite3.connect(":memory:")
    kv = KeyValueStore(conn)

    assert kv.get("theme") is None

    kv.set("theme", "dark")
    assert kv.get("theme") == "dark"

    kv.set("theme", "light")
    assert kv.get("theme") == "light"

    conn.close()
    print("KeyValueStore integration test passed successfully!")


if __name__ == "__main__":
    test_key_value_store_integration()
