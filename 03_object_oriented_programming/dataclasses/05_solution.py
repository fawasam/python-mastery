"""
Topic: Dataclass Solutions
File: 05_solution.py
"""
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass
class UserDTO:
    id: int
    email: str
    is_active: bool = True


@dataclass
class Order:
    order_id: str
    items: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.items:
            raise ValueError("Order items list cannot be empty.")


@dataclass(frozen=True)
class ConfigKey:
    section: str
    key: str


@dataclass
class APIResponseData:
    status: str
    code: int
    data: dict[str, Any] = field(default_factory=dict)

    def to_json_dict(self) -> dict[str, Any]:
        return asdict(self)


if __name__ == "__main__":
    print("--- Level 1 ---")
    u = UserDTO(1, "alice@dev.io")
    print(u)

    print("\n--- Level 2 ---")
    o = Order("ORD-101", ["Item A", "Item B"])
    print(o)

    print("\n--- Level 3 ---")
    ck = ConfigKey("database", "url")
    registry = {ck: "postgresql://localhost/db"}
    print(f"Lookup by frozen key: {registry[ck]}")

    print("\n--- Level 4 ---")
    resp = APIResponseData("SUCCESS", 200, {"user_id": 99})
    print(f"Dict output: {resp.to_json_dict()}")
