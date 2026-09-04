"""
Topic: Custom Sequence Container with __len__ and __getitem__
File: 02_examples.py
"""
from typing import Any

class CustomDeck:
    def __init__(self, items: list[Any]) -> None:
        self._items = items

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __contains__(self, item: Any) -> bool:
        return item in self._items


if __name__ == "__main__":
    deck = CustomDeck(["Ace of Spades", "King of Hearts", "Queen of Diamonds"])

    print(f"Deck length (len()): {len(deck)}")
    print(f"First item (deck[0]): {deck[0]}")
    print(f"Is 'Ace of Spades' in deck? {'Ace of Spades' in deck}")

    # Slicing works out of the box because __getitem__ delegates to list!
    print(f"Slice [1:]: {deck[1:]}")
