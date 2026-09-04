"""
SQLite Transaction Rollback on Failure.
"""

import sqlite3


def transfer_funds(conn: sqlite3.Connection, from_id: int, to_id: int, amount: float) -> None:
    try:
        # Context manager 'with conn:' begins transaction and auto-commits or rolls back
        with conn:
            # Deduct from source
            cursor = conn.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
            row = cursor.fetchone()
            if not row or row[0] < amount:
                raise ValueError(f"Insufficient funds in account {from_id}")

            conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))

            # Simulate potential error during target credit
            if to_id == 999:  # Non-existent account ID
                raise ValueError("Target account 999 does not exist")

            conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
    except ValueError as e:
        print(f"[TRANSACTION ROLLED BACK] Failed transfer: {e}")


def demo_rollback() -> None:
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL)")
        conn.execute("INSERT INTO accounts VALUES (1, 500.0), (2, 100.0)")

    print("Initial Balances:")
    for row in conn.execute("SELECT * FROM accounts"):
        print(f" Account {row[0]}: ${row[1]}")

    # Attempt failed transfer to non-existent account 999
    transfer_funds(conn, 1, 999, 200.0)

    print("\nBalances After Failed Transfer (Guaranteed Unchanged):")
    for row in conn.execute("SELECT * FROM accounts"):
        print(f" Account {row[0]}: ${row[1]}")

    conn.close()


if __name__ == "__main__":
    demo_rollback()
