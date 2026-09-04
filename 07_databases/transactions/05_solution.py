"""
Solutions for Transaction Exercises.
"""

import sqlite3


def deduct_stock_transaction(conn: sqlite3.Connection, item_id: int, qty: int) -> bool:
    try:
        with conn:
            cur = conn.execute("SELECT stock FROM inventory WHERE id = ?", (item_id,))
            row = cur.fetchone()
            if not row or row[0] < qty:
                return False
            conn.execute("UPDATE inventory SET stock = stock - ? WHERE id = ?", (qty, item_id))
        return True
    except sqlite3.Error:
        return False


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE inventory (id INTEGER PRIMARY KEY, stock INTEGER)")
        conn.execute("INSERT INTO inventory VALUES (1, 10)")

    assert deduct_stock_transaction(conn, 1, 5) is True
    assert deduct_stock_transaction(conn, 1, 10) is False  # Only 5 left!

    cur = conn.execute("SELECT stock FROM inventory WHERE id = 1")
    assert cur.fetchone()[0] == 5
    print("Stock deduction transaction exercise passed successfully!")
    conn.close()
