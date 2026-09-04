"""
Topic: Operator Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    num = 14
    is_even_and_positive = (num % 2 == 0) and (num > 0)
    print(f"Is {num} even and positive? {is_even_and_positive}")


def level_2_medium() -> None:
    total_seconds = 3665
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")


def level_3_hard(user_role: str, is_owner: bool, is_banned: bool) -> bool:
    granted = not is_banned and (user_role == "admin" or is_owner)
    print(f"Role: {user_role}, Owner: {is_owner}, Banned: {is_banned} -> Access: {granted}")
    return granted


def level_4_real_world(order_total: float, is_vip: bool, promo_code: str | None) -> float:
    discount_pct = 0.0
    if promo_code == "SAVE20":
        discount_pct = 0.20
    elif is_vip:
        discount_pct = 0.15
    elif order_total >= 500.0:
        discount_pct = 0.10

    final_total = order_total * (1.0 - discount_pct)
    print(f"Order: ${order_total:.2f} | Discount: {discount_pct:.0%} | Final: ${final_total:.2f}")
    return final_total


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard("user", True, False)
    level_3_hard("user", False, True)

    print("\n--- Level 4 ---")
    level_4_real_world(600.0, False, None)
    level_4_real_world(300.0, True, "SAVE20")
