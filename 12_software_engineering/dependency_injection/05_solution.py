"""
Solutions: Dependency Injection Exercises.
"""

from typing import Protocol


class NotifierProtocol(Protocol):
    def notify(self, msg: str) -> None:
        ...


class ConsoleNotifier:
    def notify(self, msg: str) -> None:
        print(f"[Console Notifier]: {msg}")


class OrderManager:
    """
    Refactored using Constructor Dependency Injection.
    """
    def __init__(self, notifier: NotifierProtocol) -> None:
        self.notifier = notifier

    def process(self, order_id: str) -> None:
        # Business processing logic...
        self.notifier.notify(f"Order {order_id} processed successfully.")


if __name__ == "__main__":
    notifier = ConsoleNotifier()
    manager = OrderManager(notifier)
    manager.process("ORD-999")
