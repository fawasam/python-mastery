"""
Advanced System Automation: Host System Resource Inspection.
"""

import platform
import shutil


def check_disk_usage(path: str = "/") -> dict[str, float]:
    """Inspect disk capacity and return free/total gigabytes."""
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3
    return {
        "total_gb": round(total / gb, 2),
        "used_gb": round(used / gb, 2),
        "free_gb": round(free / gb, 2),
        "percent_free": round((free / total) * 100, 1),
    }


def get_system_info() -> dict[str, str]:
    """Retrieve OS platform, machine architecture, and Python runtime version."""
    return {
        "os": platform.system(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
    }


if __name__ == "__main__":
    print("Host System Specs:", get_system_info())
    print("Root Disk Metrics:", check_disk_usage())
