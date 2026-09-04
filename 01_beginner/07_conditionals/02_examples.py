"""
Topic: Guard Clauses vs Deep Nesting
File: 02_examples.py
"""

def process_order_nested(is_authenticated: bool, has_stock: bool, balance: float, price: float) -> str:
    # ❌ DEEP NESTING ANTIPATTERN (Arrow anti-pattern)
    if is_authenticated:
        if has_stock:
            if balance >= price:
                return "Order Processed Successfully"
            else:
                return "Insufficient Funds"
        else:
            return "Item Out of Stock"
    else:
        return "User Not Authenticated"


def process_order_guard_clauses(is_authenticated: bool, has_stock: bool, balance: float, price: float) -> str:
    # ✅ CLEAN CODE: Use Guard Clauses to return early on failures
    if not is_authenticated:
        return "User Not Authenticated"
    if not has_stock:
        return "Item Out of Stock"
    if balance < price:
        return "Insufficient Funds"

    return "Order Processed Successfully"


if __name__ == "__main__":
    res1 = process_order_guard_clauses(True, True, 100.0, 50.0)
    res2 = process_order_guard_clauses(True, False, 100.0, 50.0)
    print("Test 1:", res1)
    print("Test 2:", res2)
