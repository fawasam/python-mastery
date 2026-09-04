"""
Solutions for Logging Exercises.
"""

import logging
import sys


def setup_custom_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if setup_custom_logger is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(name)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    my_logger = setup_custom_logger("PaymentService", logging.INFO)
    my_logger.info("Service initialized successfully.")
    my_logger.warning("High latency detected on endpoint.")
