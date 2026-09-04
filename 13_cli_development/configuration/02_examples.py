"""
Advanced Configuration: Reading TOML and JSON Configuration Files.
"""

import json
import tomllib


def parse_json_config(json_str: str) -> dict[str, Any]:
    """Parse JSON configuration string."""
    return json.loads(json_str)


def parse_toml_config(toml_str: str) -> dict[str, Any]:
    """Parse TOML configuration string using Python 3.11+ standard library tomllib."""
    return tomllib.loads(toml_str)


if __name__ == "__main__":
    json_data = '{"database": {"url": "sqlite:///app.db", "timeout": 30}}'
    toml_data = """
    [database]
    url = "sqlite:///app.db"
    timeout = 30
    """
    
    print("Parsed JSON Config:", parse_json_config(json_data))
    print("Parsed TOML Config:", parse_toml_config(toml_data))
