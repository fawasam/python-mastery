"""
Common Mistakes in Database Transactions.
"""

import sqlite3


# MISTAKE: Long-running transactions holding table locks
def mistake_long_transaction(conn: sqlite3.Connection) -> None:
    # DANGER: Opening a transaction and performing long network I/O or sleep
    # keeps database table locks open, blocking all other connections from writing!
    pass


if __name__ == "__main__":
    print("Keep database transactions as short and fast as possible to avoid lock contention!")
