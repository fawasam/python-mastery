"""
Logging Exception Stack Traces and Custom Handlers.
"""

import logging
import sys

# Instantiate modular logger
logger = logging.getLogger("AppService")
logger.setLevel(logging.INFO)

# Create console handler printing to stdout
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def divide_and_log(a: float, b: float) -> float | None:
    logger.info("Initiating division operation for %f / %f", a, b)
    try:
        return a / b
    except ZeroDivisionError:
        # logger.exception automatically captures and formats the current exception traceback!
        logger.exception("Division operation failed due to zero denominator.")
        return None


if __name__ == "__main__":
    divide_and_log(10.0, 2.0)
    divide_and_log(10.0, 0.0)
