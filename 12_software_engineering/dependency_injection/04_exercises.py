"""
Exercises: Refactoring to Dependency Injection.
"""

from typing import Protocol


class NotifierProtocol(Protocol):
    def notify(self, msg: str) -> None:
        ...


class OrderManager:
    """
    Exercise: Refactor OrderManager to use constructor injection of NotifierProtocol.
    
    Level 1 - Easy
    """
    def __init__(self, notifier: NotifierProtocol) -> None:
        raise NotImplementedError("Implement constructor DI for OrderManager")

    def process(self, order_id: str) -> None:
        raise NotImplementedError("Implement order processing with injected notifier")
