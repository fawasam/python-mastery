"""
Topic: Variables & Dynamic Typing
File: 05_solution.py

Official solutions for 04_exercises.py.
"""
from typing import Any

def level_1_easy() -> None:
    product_name: str = "Mechanical Keyboard"
    unit_price: float = 89.99
    stock_quantity: int = 42

    print(f"Product: {product_name} | Price: ${unit_price} | Stock: {stock_quantity} units")


def level_2_medium() -> None:
    primary_color = "Blue"
    secondary_color = "Red"

    # Idiomatic variable swapping in Python
    primary_color, secondary_color = secondary_color, primary_color

    print(f"Swapped colors -> Primary: {primary_color}, Secondary: {secondary_color}")


def level_3_hard() -> None:
    flexible_var: Any = 100
    print(f"Int value: {flexible_var} | Type: {type(flexible_var)} | Memory ID: {id(flexible_var)}")

    flexible_var = [1, 2, 3]
    print(f"List value: {flexible_var} | Type: {type(flexible_var)} | Memory ID: {id(flexible_var)}")


def level_4_real_world() -> dict[str, Any]:
    DB_HOST: str = "db.internal.production"
    DB_PORT: int = 5432
    DB_USER: str = "service_admin"
    IS_SSL_ENABLED: bool = True

    config = {
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
        "ssl": IS_SSL_ENABLED,
    }
    print(f"Database Config: {config}")
    return config


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()
    print("\n--- Level 2 ---")
    level_2_medium()
    print("\n--- Level 3 ---")
    level_3_hard()
    print("\n--- Level 4 ---")
    level_4_real_world()
