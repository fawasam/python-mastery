"""
Mini-Project 01: Personal Finance & Expense Tracker CLI
File: main.py

A complete, runnable CLI application demonstrating all beginner Python concepts:
variables, data types, control flow, functions, dictionaries, exception handling, and file persistence.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Path to local storage file
STORAGE_FILE = Path(__file__).parent / "transactions.json"


def load_transactions() -> list[dict[str, Any]]:
    """Load stored transactions from JSON file."""
    if not STORAGE_FILE.exists():
        return []
    try:
        with STORAGE_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Warning: Could not read storage file ({e}). Starting with empty record.")
        return []


def save_transactions(transactions: list[dict[str, Any]]) -> None:
    """Save transactions to JSON file."""
    try:
        with STORAGE_FILE.open("w", encoding="utf-8") as f:
            json.dump(transactions, f, indent=2)
        print("💾 Transactions saved successfully.")
    except OSError as e:
        print(f"❌ Error saving transactions: {e}")


def add_transaction(transactions: list[dict[str, Any]], t_type: str, category: str, amount: float) -> None:
    """Validate and record a new transaction."""
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    
    t_type_upper = t_type.strip().upper()
    if t_type_upper not in ("INCOME", "EXPENSE"):
        raise ValueError("Type must be either 'INCOME' or 'EXPENSE'.")

    entry = {
        "id": len(transactions) + 1,
        "type": t_type_upper,
        "category": category.strip().title(),
        "amount": round(amount, 2),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
    }
    transactions.append(entry)
    print(f"✅ Added {entry['type']}: {entry['category']} (${entry['amount']:.2f})")


def calculate_summary(transactions: list[dict[str, Any]]) -> dict[str, float]:
    """Compute income, expense, balance, and savings rate."""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "INCOME")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "EXPENSE")
    net_balance = total_income - total_expense
    savings_rate = ((total_income - total_expense) / total_income * 100) if total_income > 0 else 0.0

    return {
        "total_income": round(total_income, 2),
        "total_expense": round(total_expense, 2),
        "net_balance": round(net_balance, 2),
        "savings_rate": round(savings_rate, 1),
    }


def print_summary_report(transactions: list[dict[str, Any]]) -> None:
    """Print financial summary dashboard."""
    summary = calculate_summary(transactions)
    print("\n" + "=" * 45)
    print("         FINANCIAL SUMMARY DASHBOARD         ")
    print("=" * 45)
    print(f"Total Income:     ${summary['total_income']:>12,.2f}")
    print(f"Total Expenses:   ${summary['total_expense']:>12,.2f}")
    print(f"Net Balance:      ${summary['net_balance']:>12,.2f}")
    print(f"Savings Rate:      {summary['savings_rate']:>11.1f}%")
    print("=" * 45 + "\n")


def print_category_breakdown(transactions: list[dict[str, Any]]) -> None:
    """Print expenses grouped by category."""
    expense_categories: dict[str, float] = {}
    for t in transactions:
        if t["type"] == "EXPENSE":
            cat = t["category"]
            expense_categories[cat] = expense_categories.get(cat, 0.0) + t["amount"]

    print("\n" + "-" * 35)
    print(f"{'CATEGORY':<20} | {'AMOUNT ($)':>10}")
    print("-" * 35)
    if not expense_categories:
        print("No expenses recorded yet.")
    else:
        for cat, total in sorted(expense_categories.items(), key=lambda x: x[1], reverse=True):
            print(f"{cat:<20} | ${total:>10.2f}")
    print("-" * 35 + "\n")


def run_demo_mode() -> None:
    """Non-interactive test run for verification."""
    print("--- Running Expense Tracker Demo Mode ---")
    txs: list[dict[str, Any]] = []
    
    add_transaction(txs, "INCOME", "Salary", 4500.00)
    add_transaction(txs, "INCOME", "Freelance", 800.00)
    add_transaction(txs, "EXPENSE", "Housing Rent", 1600.00)
    add_transaction(txs, "EXPENSE", "Groceries", 450.00)
    add_transaction(txs, "EXPENSE", "Utilities", 180.00)
    add_transaction(txs, "EXPENSE", "Dining Out", 120.00)

    print_summary_report(txs)
    print_category_breakdown(txs)
    save_transactions(txs)


if __name__ == "__main__":
    run_demo_mode()
