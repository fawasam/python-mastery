"""
Architecture Anti-Patterns: Anemic Domain Model & Leaky Abstractions.
"""


class AnemicOrder:
    """
    MISTAKE: Anemic Domain Model.
    
    Why: Holds only public attributes with zero business logic.
    Business rules get leaked into random controller or service functions instead of living inside the domain entity.
    """
    def __init__(self, order_id: str, status: str, items: list[float]) -> None:
        self.order_id = order_id
        self.status = status
        self.items = items


# Bad practice: Controller function mutating domain object attributes directly
def bad_cancel_order(order: AnemicOrder) -> None:
    if order.status == "SHIPPED":
        raise ValueError("Cannot cancel shipped order")
    order.status = "CANCELLED"  # Direct attribute mutation outside domain entity!


if __name__ == "__main__":
    print("Architecture anti-pattern demonstration module.")
