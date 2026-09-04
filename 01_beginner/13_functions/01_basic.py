"""
Topic: Function Basics & Type Annotations
File: 01_basic.py
"""

def calculate_invoice_total(subtotal: float, tax_rate: float = 0.08, discount: float = 0.0) -> float:
    """
    Calculate the final invoice total after applying discount and tax.

    Args:
        subtotal: Pre-tax order amount.
        tax_rate: Sales tax rate (default 8%).
        discount: Fixed dollar discount.

    Returns:
        Final amount payable.
    """
    discounted_subtotal = max(0.0, subtotal - discount)
    tax_amount = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax_amount
    return round(total, 2)


if __name__ == "__main__":
    # Standard call using defaults
    total_1 = calculate_invoice_total(100.0)
    print(f"Standard invoice total: ${total_1:.2f}")

    # Keyword argument call overriding defaults
    total_2 = calculate_invoice_total(subtotal=200.0, discount=25.0, tax_rate=0.10)
    print(f"Discounted invoice total: ${total_2:.2f}")
