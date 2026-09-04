"""
Transaction Exercises.
"""

import sqlite3


# Exercise 1 (Medium): Safe Stock Deduction Transaction
# Write deduct_stock_transaction(conn: sqlite3.Connection, item_id: int, qty: int) -> bool
# Table 'inventory' has columns (id INTEGER PRIMARY KEY, stock INTEGER).
# Deducts 'qty' from item_id ONLY IF current stock >= qty. Returns True on success, False if stock insufficient.
def deduct_stock_transaction(conn: sqlite3.Connection, item_id: int, qty: int) -> bool:
    raise NotImplementedError("Implement deduct_stock_transaction")
