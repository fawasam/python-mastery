"""
Topic: Factory Constructors with @classmethod
File: 01_basic.py
"""
from typing import Any, Self

class Configuration:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """Factory constructor instantiating Configuration from a dictionary."""
        return cls(host=data.get("host", "localhost"), port=int(data.get("port", 8080)))

    @classmethod
    def default(cls) -> Self:
        """Factory constructor instantiating default Configuration."""
        return cls(host="127.0.0.1", port=8000)


if __name__ == "__main__":
    c1 = Configuration.from_dict({"host": "prod.server", "port": 9000})
    c2 = Configuration.default()

    print(f"c1: {c1.host}:{c1.port}")
    print(f"c2: {c2.host}:{c2.port}")
