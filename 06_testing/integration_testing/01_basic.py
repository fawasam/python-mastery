"""
Basic Integration Test using In-Memory SQLite Database.
"""

import sqlite3


class UserDatabase:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

    def add_user(self, name: str) -> int:
        with self.conn:
            cursor = self.conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
            return cursor.lastrowid

    def get_user_count(self) -> int:
        cursor = self.conn.execute("SELECT COUNT(*) FROM users")
        return cursor.fetchone()[0]


def test_user_database_integration() -> None:
    # Use SQLite in-memory database for fast, real SQL integration testing
    conn = sqlite3.connect(":memory:")
    db = UserDatabase(conn)

    assert db.get_user_count() == 0

    user_id1 = db.add_user("Alice")
    user_id2 = db.add_user("Bob")

    assert user_id1 == 1
    assert user_id2 == 2
    assert db.get_user_count() == 2

    conn.close()
    print("In-memory SQLite integration test passed successfully!")


if __name__ == "__main__":
    test_user_database_integration()
