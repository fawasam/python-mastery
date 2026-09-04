"""
Solutions: System Automation Exercises.
"""

import shutil


def is_disk_space_sufficient(min_free_gb: float) -> bool:
    _, _, free_bytes = shutil.disk_usage("/")
    free_gb = free_bytes / (1024 ** 3)
    return free_gb >= min_free_gb


if __name__ == "__main__":
    print("Has at least 1 GB free space?", is_disk_space_sufficient(1.0))
