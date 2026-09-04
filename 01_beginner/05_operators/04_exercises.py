"""
Topic: Operator Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write an expression that checks if an integer `num` is even AND positive.
    """
    num = 14
    # TODO: Evaluate even and positive condition
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Convert total seconds (e.g. `3665`) into hours, minutes, and remaining seconds using floor division (`//`) and modulus (`%`).
    """
    total_seconds = 3665
    # TODO: Calculate hours, minutes, seconds
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement an access decision function `can_access_resource(user_role, is_owner, is_banned)`.
    Access is granted if user is NOT banned, AND (user is an 'admin' OR user is the 'owner').
    """
    # TODO: Implement rule using logical operators
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Write a discount calculator function `calculate_discount(order_total, is_vip, promo_code)`.
    - If VIP, default 15% discount.
    - If promo_code is "SAVE20", add 20% discount (cannot combine with VIP; promo code takes precedence).
    - If order_total >= 500 and not VIP/promo, grant 10% discount.
    - Otherwise 0%.
    Return final order total after applying discount.
    """
    # TODO: Calculate final discounted price
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
