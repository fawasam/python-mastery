"""
Real-world Examples of Python Closures: Configurable Logger and Moving Average Calculator.
"""

from typing import Callable


def make_logger(prefix: str) -> Callable[[str], None]:
    """
    Returns a custom logger function pre-configured with a specific prefix string.
    """

    def log(message: str) -> None:
        print(f"[{prefix.upper()}] {message}")

    return log


def make_moving_average() -> Callable[[float], float]:
    """
    Returns a closure that maintains a running average of all numbers passed to it.
    """
    numbers: list[float] = []

    def averager(new_value: float) -> float:
        # Note: We don't need 'nonlocal' here because we are mutating the list (append),
        # not reassigning the variable name 'numbers'.
        numbers.append(new_value)
        return sum(numbers) / len(numbers)

    return averager


if __name__ == "__main__":
    info_log = make_logger("INFO")
    error_log = make_logger("ERROR")

    info_log("Application started successfully.")
    error_log("Database connection failed.")

    avg = make_moving_average()
    print(f"Average after 10: {avg(10.0)}")  # 10.0
    print(f"Average after 20: {avg(20.0)}")  # 15.0
    print(f"Average after 30: {avg(30.0)}")  # 20.0
