"""
Topic: OS and Sys Solutions
File: 05_solution.py
"""
import os
import sys
from typing import Any

def level_1_easy() -> int:
    port_str = os.getenv("PORT", "8080")
    try:
        port = int(port_str)
    except ValueError:
        port = 8080
    print(f"Server Port: {port}")
    return port


def level_2_medium(mock_argv: list[str] | None = None) -> None:
    args = mock_argv if mock_argv is not None else sys.argv[1:]
    print("CLI Arguments:")
    for idx, arg in enumerate(args, 1):
        print(f"  Arg {idx}: {arg}")


def level_3_hard() -> dict[str, Any]:
    info = {
        "os_name": os.name,
        "platform": sys.platform,
        "python_version": sys.version.split()[0],
        "process_id": os.getpid(),
    }
    print(f"System Info: {info}")
    return info


def bootstrap_env(required_keys: list[str]) -> bool:
    missing = [k for k in required_keys if k not in os.environ]
    if missing:
        print(f"❌ Error: Missing required env keys: {missing}", file=sys.stderr)
        return False
    print("✅ All required environment variables present.")
    return True


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium(["--config", "prod.yaml", "--verbose"])

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    os.environ["DATABASE_URL"] = "postgresql://localhost/db"
    bootstrap_env(["DATABASE_URL"])
