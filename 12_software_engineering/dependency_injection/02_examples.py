"""
Advanced Dependency Injection: Building a Simple Inversion of Control (IoC) Container.
"""

from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")


class Container:
    """Simple IoC / DI Container managing component registration and resolution."""
    def __init__(self) -> None:
        self._providers: dict[Type[Any], Callable[[], Any]] = {}

    def register(self, interface: Type[T], provider: Callable[[], T]) -> None:
        """Register a factory/provider function for an interface."""
        self._providers[interface] = provider

    def resolve(self, interface: Type[T]) -> T:
        """Resolve an instance for the given interface type."""
        if interface not in self._providers:
            raise KeyError(f"No provider registered for {interface}")
        return self._providers[interface]()


# --- Example Domain Classes ---

class PaymentGateway:
    def process_charge(self, amount: float) -> bool:
        print(f"Charged ${amount} via PaymentGateway")
        return True


class OrderProcessor:
    def __init__(self, gateway: PaymentGateway) -> None:
        self.gateway = gateway

    def place_order(self, amount: float) -> None:
        if self.gateway.process_charge(amount):
            print("Order successfully placed!")


if __name__ == "__main__":
    container = Container()
    
    # Register dependencies
    container.register(PaymentGateway, lambda: PaymentGateway())
    container.register(OrderProcessor, lambda: OrderProcessor(container.resolve(PaymentGateway)))
    
    # Resolve top-level object with auto-wired dependencies
    processor = container.resolve(OrderProcessor)
    processor.place_order(99.99)
