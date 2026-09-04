"""
Common Mistakes in Python Logging.
"""

import logging

logger = logging.getLogger(__name__)


# MISTAKE 1: Eager string formatting in log calls
def mistake_eager_formatting(user_id: int, heavy_data: str) -> None:
    # DANGER: f-string evaluates heavy_data regardless of whether DEBUG level is enabled!
    logger.debug(f"User {user_id} payload: {heavy_data}")


# GOOD PRACTICE: Lazy string interpolation
def good_lazy_formatting(user_id: int, heavy_data: str) -> None:
    # Formatting string is evaluated ONLY if DEBUG level is enabled by subscriber handler!
    logger.debug("User %d payload: %s", user_id, heavy_data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # DEBUG messages disabled!
    good_lazy_formatting(101, "Data Payload")
    print("Logged with lazy formatting successfully.")
