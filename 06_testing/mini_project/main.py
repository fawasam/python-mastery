"""
Financial Transaction Engine & Automated Test Suite.
"""

import sqlite3
from typing import Protocol
from unittest.mock import MagicMock


# 1. CURRENCY EXCHANGE ADAPTER PROTOCOL
class CurrencyExchangeAdapter(Protocol):
    def get_rate(self, base: str, target: str) -> float:
        ...


# 2. TRANSACTION ENGINE SERVICE
class BankingService:
    def __init__(self, conn: sqlite3.Connection, exchange_adapter: CurrencyExchangeAdapter) -> None:
        self.conn = conn
        self.exchange_adapter = exchange_adapter
        self._init_db()

    def _init_db(self) -> None:
        with self.conn:
            self.conn.execute("CREATE TABLE IF NOT EXISTS accounts (account_id TEXT PRIMARY KEY, balance REAL)")

    def create_account(self, account_id: str, initial_balance: float) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        with self.conn:
            self.conn.execute("INSERT INTO accounts (account_id, balance) VALUES (?, ?)", (account_id, initial_balance))

    def get_balance(self, account_id: str) -> float:
        cur = self.conn.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cur.fetchone()
        if not row:
            raise KeyError(f"Account '{account_id}' not found")
        return row[0]

    def transfer_foreign(self, sender_id: str, receiver_id: str, amount_usd: float, target_currency: str) -> float:
        sender_bal = self.get_balance(sender_id)
        if sender_bal < amount_usd:
            raise ValueError("Insufficient balance")

        rate = self.exchange_adapter.get_rate("USD", target_currency)
        converted_amount = round(amount_usd * rate, 2)

        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount_usd, sender_id))
            self.conn.execute(
                "UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (converted_amount, receiver_id)
            )

        return converted_amount


# 3. TEST SUITE DEMONSTRATION
def test_banking_service_full_suite() -> None:
    # Set up in-memory database & mock exchange adapter
    conn = sqlite3.connect(":memory:")
    mock_exchange = MagicMock(spec=CurrencyExchangeAdapter)
    mock_exchange.get_rate.return_value = 0.85  # USD to EUR mock rate

    service = BankingService(conn, mock_exchange)

    # 1. Create accounts
    service.create_account("ACC-101", 500.0)
    service.create_account("ACC-102", 100.0)
    assert service.get_balance("ACC-101") == 500.0

    # 2. Perform foreign transfer
    converted = service.transfer_foreign("ACC-101", "ACC-102", 200.0, "EUR")
    assert converted == 170.0  # 200 * 0.85

    assert service.get_balance("ACC-101") == 300.0
    assert service.get_balance("ACC-102") == 270.0  # 100 + 170

    mock_exchange.get_rate.assert_called_once_with("USD", "EUR")

    conn.close()
    print("Full BankingService automated test suite passed successfully!")


if __name__ == "__main__":
    test_banking_service_full_suite()
