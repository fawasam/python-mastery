"""
Topic: Lambda Solutions
File: 05_solution.py
"""
from typing import Any, Callable

def level_1_easy() -> list[str]:
    words = ["apple", "fig", "banana", "kiwi"]
    sorted_words = sorted(words, key=lambda w: len(w))
    print(f"Sorted by length: {sorted_words}")
    return sorted_words


def level_2_medium() -> list[tuple[int, int]]:
    coords = [(1, 5), (3, 2), (2, 8)]
    sorted_coords = sorted(coords, key=lambda pt: pt[1])
    print(f"Sorted by second item: {sorted_coords}")
    return sorted_coords


def level_3_hard(products: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Compound key: (not in_stock, price) -> In-stock (False first), then price ascending
    sorted_prods = sorted(products, key=lambda p: (not p["in_stock"], p["price"]))
    print("Multi-key sorted products:")
    for p in sorted_prods:
        print(f"  - {p['name']}: ${p['price']} (In Stock: {p['in_stock']})")
    return sorted_prods


class EventRegistry:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[..., None]]] = {}

    def subscribe(self, event: str, handler: Callable[..., None]) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def publish(self, event: str, payload: Any) -> None:
        for handler in self._handlers.get(event, []):
            handler(payload)


def level_4_real_world() -> None:
    bus = EventRegistry()
    bus.subscribe("USER_REGISTERED", lambda data: print(f"[Audit Log] User {data['id']} registered."))
    bus.subscribe("USER_REGISTERED", lambda data: print(f"[Email Service] Sending welcome to {data['email']}."))

    bus.publish("USER_REGISTERED", {"id": 104, "email": "newuser@dev.io"})


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    prods = [
        {"name": "Mouse", "price": 25.0, "in_stock": False},
        {"name": "Monitor", "price": 300.0, "in_stock": True},
        {"name": "Keyboard", "price": 80.0, "in_stock": True},
    ]
    level_3_hard(prods)

    print("\n--- Level 4 ---")
    level_4_real_world()
