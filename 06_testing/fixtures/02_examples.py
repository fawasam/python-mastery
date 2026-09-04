"""
Fixture Composition: Chaining Multiple Fixtures Together.
"""

from typing import Generator


def raw_config_fixture() -> dict[str, str]:
    return {"host": "localhost", "port": "5432"}


def connection_string_fixture() -> str:
    cfg = raw_config_fixture()
    return f"postgresql://{cfg['host']}:{cfg['port']}/test_db"


def test_connection_string_builder() -> None:
    conn_str = connection_string_fixture()
    assert conn_str == "postgresql://localhost:5432/test_db"


if __name__ == "__main__":
    test_connection_string_builder()
    print("Fixture composition test passed!")
