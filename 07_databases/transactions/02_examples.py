"""
Nested Transactions and Savepoints in SQLite.
"""

import sqlite3


def demo_savepoint() -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE log (message TEXT)")

    conn.execute("BEGIN TRANSACTION")
    conn.execute("INSERT INTO log VALUES ('Step 1: Main Order Created')")

    # Create a Savepoint
    conn.execute("SAVEPOINT optional_discount")
    conn.execute("INSERT INTO log VALUES ('Step 2: Applied 10% Discount')")

    # Decide to roll back only to savepoint
    conn.execute("ROLLBACK TO SAVEPOINT optional_discount")

    # Commit main transaction
    conn.execute("COMMIT")

    rows = [r[0] for r in conn.execute("SELECT message FROM log")]
    print("Log Messages After Savepoint Rollback:")
    for msg in rows:
        print(f" - {msg}")

    assert len(rows) == 1
    assert "Step 2" not in rows[0]
    conn.close()


if __name__ == "__main__":
    demo_savepoint()
