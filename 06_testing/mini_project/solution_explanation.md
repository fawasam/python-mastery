# Solution Explanation: Banking Service & Automated Test Suite

## Testing Architectural Design

1. **In-Memory Integration (`sqlite3.connect(":memory:")`)**:
   Instead of mocking SQL queries, `BankingService` runs real transactions against an in-memory SQLite database, verifying SQL syntax, constraints, and atomic multi-row updates.

2. **Mocking External Dependents (`MagicMock(spec=CurrencyExchangeAdapter)`)**:
   External currency exchange rates are volatile and depend on network APIs. Using `MagicMock` isolates the business transfer logic from network flakiness.

3. **Call Assertion Verification (`assert_called_once_with`)**:
   Verifies that the banking service queried the exchange rate with the exact base ("USD") and target ("EUR") currency parameters.
