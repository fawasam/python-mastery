"""
Basic Transaction Atomicity and Rollback in SQLite.
"""

import sqlite3


def execute_atomic_batch(conn: sqlite3.Connection, operations: list[tuple[str, str]]) -> bool:
    """
    Executes multiple SQL operations inside an atomic transaction.
    Rolls back ALL operations if any single item fails.
    """
    try:
        with conn:
            for query, params in operations:
                conn.execute(query, (params,))
        return True
    except sqlite3.Error as e:
        print(f"[TRANSACTION FAILED & ROLLED BACK] {e}")
        return False


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE inventory (sku TEXT PRIMARY KEY)")

    valid_ops = [
        ("INSERT INTO inventory VALUES (?)", "SKU-1"),
        ("INSERT INTO inventory VALUES (?)", "SKU-2"),
    ]
    assert execute_atomic_batch(conn, valid_ops) is True

    invalid_ops = [
        ("INSERT INTO inventory VALUES (?)", "SKU-3"),
        ("INSERT INTO inventory VALUES (?)", "SKU-1"),  # Primary Key Constraint Failure!
    ]
    assert execute_atomic_batch(conn, invalid_ops) is False

    # Verify SKU-3 was ROLLED BACK and does NOT exist in table!
    cur = conn.execute("SELECT COUNT(*) FROM inventory WHERE sku = 'SKU-3'")
    assert cur.fetchone()[0] == 0
    print("Atomic transaction rollback verified successfully!")
    conn.close()
