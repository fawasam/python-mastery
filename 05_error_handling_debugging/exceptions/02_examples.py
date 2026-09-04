"""
Exception Chaining and Translation in Python.
"""


class DatabaseConnectionError(Exception):
    """Custom application exception."""

    pass


def connect_raw_socket(host: str, port: int) -> None:
    if host == "invalid.local":
        raise OSError("DNS Resolution Failed")


def initialize_database_session(host: str, port: int) -> None:
    try:
        connect_raw_socket(host, port)
    except OSError as err:
        # Exception Chaining: 'raise ... from err' links the low-level cause to high-level domain error
        raise DatabaseConnectionError(f"Failed to connect to DB host '{host}:{port}'") from err


if __name__ == "__main__":
    try:
        initialize_database_session("invalid.local", 5432)
    except DatabaseConnectionError as db_err:
        print(f"Caught Application Error: {db_err}")
        print(f"Original Root Cause: {db_err.__cause__}")
