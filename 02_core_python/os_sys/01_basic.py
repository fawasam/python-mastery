"""
Topic: OS & Sys Module Fundamentals
File: 01_basic.py
"""
import os
import sys

def demonstrate_os_and_sys() -> None:
    # 1. Reading Environment Variables with os.getenv (Safe fallback)
    app_env = os.getenv("APP_ENV", "development")
    api_key = os.getenv("API_KEY", "NOT_CONFIGURED")

    print(f"Environment: {app_env}")
    print(f"API Key:     {api_key}")

    # 2. System info & sys.argv
    print(f"\nProcess ID (PID): {os.getpid()}")
    print(f"Python Executable: {sys.executable}")
    print(f"CLI Arguments:    {sys.argv}")


if __name__ == "__main__":
    demonstrate_os_and_sys()
