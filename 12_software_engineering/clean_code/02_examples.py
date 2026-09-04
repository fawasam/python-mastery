"""
Clean Code Advanced Techniques: Small Functions & Parameter Objects.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerOrder:
    """Parameter object encapsulating order details."""
    order_id: str
    items: list[dict[str, float]]
    discount_code: str | None
    shipping_country: str


class OrderCalculator:
    """Calculates order totals cleanly by delegating steps to focused helper methods."""
    
    TAX_RATES: dict[str, float] = {
        "US": 0.08,
        "CA": 0.12,
        "DE": 0.19,
    }
    
    def calculate_order_total(self, order: CustomerOrder) -> float:
        """
        Main calculation orchestrator.
        
        Why: Delegates sub-tasks to private single-purpose methods.
        """
        subtotal = self._calculate_subtotal(order.items)
        discount = self._apply_discount(subtotal, order.discount_code)
        tax = self._calculate_tax(subtotal - discount, order.shipping_country)
        
        return (subtotal - discount) + tax

    def _calculate_subtotal(self, items: list[dict[str, float]]) -> float:
        return sum(item["price"] * item.get("quantity", 1) for item in items)

    def _apply_discount(self, subtotal: float, discount_code: str | None) -> float:
        if discount_code == "SAVE10":
            return subtotal * 0.10
        if discount_code == "SAVE20":
            return subtotal * 0.20
        return 0.0

    def _calculate_tax(self, taxable_amount: float, country: str) -> float:
        rate = self.TAX_RATES.get(country, 0.05)
        return taxable_amount * rate


if __name__ == "__main__":
    order = CustomerOrder(
        order_id="ORD-1001",
        items=[{"name": "Laptop", "price": 1000.0, "quantity": 1}],
        discount_code="SAVE10",
        shipping_country="US"
    )
    
    calc = OrderCalculator()
    total = calc.calculate_order_total(order)
    print(f"Total order price for {order.order_id}: ${total:.2f}")
