"""
Pytest Data Model and Dictionary Testing.
"""


def calculate_cart_total(items: list[dict[str, float]]) -> float:
    total = sum(item["price"] * item["quantity"] for item in items)
    return round(total, 2)


def test_calculate_cart_total_single_item() -> None:
    cart = [{"price": 10.50, "quantity": 2}]
    assert calculate_cart_total(cart) == 21.00


def test_calculate_cart_total_multiple_items() -> None:
    cart = [
        {"price": 10.50, "quantity": 2},  # 21.00
        {"price": 5.25, "quantity": 4},  # 21.00
    ]
    assert calculate_cart_total(cart) == 42.00


if __name__ == "__main__":
    test_calculate_cart_total_single_item()
    test_calculate_cart_total_multiple_items()
    print("Cart calculation tests passed successfully!")
