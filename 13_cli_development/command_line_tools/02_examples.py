"""
Advanced CLI Tooling: Progress Indicators with Rich.
"""

import time
from rich.progress import track


def simulate_download_task() -> None:
    """Simulate CLI task with animated terminal progress bar."""
    print("Starting batch item download...")
    items = range(10)
    for _ in track(items, description="Downloading items..."):
        time.sleep(0.05)
    print("All downloads finished!")


if __name__ == "__main__":
    simulate_download_task()
