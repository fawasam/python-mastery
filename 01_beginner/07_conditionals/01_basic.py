"""
Topic: Conditionals & Control Flow Basics
File: 01_basic.py
"""

def evaluate_temperature(temp_celsius: float) -> None:
    print(f"Current Temperature: {temp_celsius}°C")
    
    # 1. Standard if-elif-else branching
    if temp_celsius < 0:
        status = "Freezing"
    elif temp_celsius < 15:
        status = "Cold"
    elif temp_celsius < 25:
        status = "Mild/Comfortable"
    elif temp_celsius < 35:
        status = "Warm"
    else:
        status = "Hot"

    print(f"Weather status: {status}")

    # 2. Ternary Operator Expression
    # Assigning value based on a single condition cleanly
    is_freezing = True if temp_celsius <= 0 else False
    print(f"Is freezing flag: {is_freezing}")


if __name__ == "__main__":
    evaluate_temperature(22.5)
    evaluate_temperature(-4.0)
