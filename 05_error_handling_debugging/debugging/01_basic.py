"""
Basic Interactive Debugging using Traceback and Programmatic Debugging.
"""

import traceback


def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"Discount percentage must be between 0 and 100, got {discount_percent}")
    return price * (1.0 - discount_percent / 100.0)


def process_order(price: float, discount_percent: float) -> float | None:
    try:
        return calculate_discount(price, discount_percent)
    except ValueError as e:
        print("[DEBUG] Exception caught. Formatting stack traceback:")
        # Programmatically inspect and format traceback string without crashing application
        formatted_tb = traceback.format_exc()
        print(formatted_tb)
        return None


if __name__ == "__main__":
    print("--- Normal Calculation ---")
    res1 = process_order(100.0, 20.0)
    print(f"Final Price: ${res1}")

    print("\n--- Triggering Debug Traceback ---")
    res2 = process_order(100.0, 150.0)
