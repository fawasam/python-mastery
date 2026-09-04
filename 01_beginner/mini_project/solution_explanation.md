# Mini-Project 01 — Solution Explanation

## Architecture Overview
The Personal Finance & Expense Tracker is structured cleanly into functional layers:

1. **Persistence Layer**:
   - `load_transactions()` and `save_transactions()` handle reading and writing to disk using `pathlib.Path` and JSON serialization (`json.dump` / `json.load`).
   - Uses `try-except` blocks to handle missing or corrupt file errors gracefully.

2. **Domain Business Logic**:
   - `add_transaction()` validates user input (positive amounts, valid `INCOME`/`EXPENSE` types) before appending to the transactions list.
   - `calculate_summary()` aggregates total income, total expenses, net balance, and calculates savings rate as a percentage (`(income - expense) / income * 100`).

3. **Presentation Layer**:
   - `print_summary_report()` formats outputs using tabular alignment and f-string number formatting (`${total:,.2f}`).
   - `print_category_breakdown()` groups expenses by category using a Python dictionary accumulator and sorts categories descending by total spent.

## Testing & Verification
Run the demo script to verify all operations:
```bash
python 01_beginner/mini_project/main.py
```
