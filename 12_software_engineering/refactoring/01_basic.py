"""
Refactoring Basics: Extract Method & Primitive Obsession Refactoring.
"""

from dataclasses import dataclass


# --- BEFORE REFACTORING ---
def calculate_and_print_statement_dirty(name: str, email: str, street: str, city: str, zip_code: str, items: list[tuple[str, float]]) -> None:
    # Code smell: Primitive Obsession & Long Method
    subtotal = 0.0
    for item_name, price in items:
        subtotal += price
        
    tax = subtotal * 0.10
    total = subtotal + tax
    
    print(f"--- STATEMENT FOR {name} ({email}) ---")
    print(f"Address: {street}, {city} {zip_code}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Due: ${total:.2f}")


# --- AFTER REFACTORING ---

@dataclass(frozen=True)
class CustomerAddress:
    street: str
    city: str
    zip_code: str


@dataclass(frozen=True)
class CustomerInfo:
    name: str
    email: str
    address: CustomerAddress


def calculate_totals(items: list[tuple[str, float]], tax_rate: float = 0.10) -> tuple[float, float, float]:
    """Extracted Method: Responsible only for math calculations."""
    subtotal = sum(price for _, price in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total


def render_statement(customer: CustomerInfo, subtotal: float, tax: float, total: float) -> str:
    """Extracted Method: Responsible only for statement formatting."""
    addr = customer.address
    return (
        f"--- STATEMENT FOR {customer.name} ({customer.email}) ---\n"
        f"Address: {addr.street}, {addr.city} {addr.zip_code}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Total Due: ${total:.2f}"
    )


if __name__ == "__main__":
    customer = CustomerInfo(
        name="Bob Smith",
        email="bob@example.com",
        address=CustomerAddress("123 Main St", "Springfield", "90210")
    )
    items = [("Widget", 25.0), ("Gadget", 75.0)]
    
    subtotal, tax, total = calculate_totals(items)
    output = render_statement(customer, subtotal, tax, total)
    print(output)
