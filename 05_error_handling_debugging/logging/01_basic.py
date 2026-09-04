"""
Basic Python Logging Configuration.
"""

import logging

# Configure basic logging formatting and level threshold
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Best Practice: Use getLogger(__name__) to establish module hierarchy
logger = logging.getLogger(__name__)


def run_logging_demo() -> None:
    logger.debug("Debugging details for developers.")
    logger.info("Application event: Service started.")
    logger.warning("Resource usage warning: Disk space at 85%.")
    logger.error("Operation failed: Database connection timed out.")
    logger.critical("System failure: Out of memory!")


if __name__ == "__main__":
    run_logging_demo()
