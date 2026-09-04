"""
Topic: Advanced Output Formatting Examples
File: 02_examples.py
"""

def demonstrate_table_formatting() -> None:
    # Creating a formatted tabular output with padding and alignment
    products = [
        ("Laptop Pro", 1299.99, 15),
        ("Wireless Mouse", 24.50, 150),
        ("USB-C Hub", 49.90, 85),
        ("4K Monitor", 449.00, 8),
    ]

    print(f"{'PRODUCT NAME':<20} | {'PRICE ($)':>10} | {'STOCK':>6}")
    print("-" * 43)

    for item, price, stock in products:
        print(f"{item:<20} | {price:>10.2f} | {stock:>6d}")

    # Percentage formatting
    completion_rate = 0.8745
    print(f"\nTask Completion Rate: {completion_rate:.1%}")


if __name__ == "__main__":
    demonstrate_table_formatting()
