"""
Topic: Graceful CLI Exit Handlers
File: 02_examples.py
"""
import os
import sys

def validate_environment() -> None:
    required_vars = ["APP_ENV"]
    missing = [var for var in required_vars if var not in os.environ]

    if missing:
        print(f"❌ Error: Missing required environment variables: {missing}", file=sys.stderr)
        # Non-zero exit code signals failure to shell scripts / Docker containers
        sys.exit(1)

    print("✅ Environment configuration validated successfully.")


if __name__ == "__main__":
    # Temporarily set variable for test pass
    os.environ["APP_ENV"] = "production"
    validate_environment()
