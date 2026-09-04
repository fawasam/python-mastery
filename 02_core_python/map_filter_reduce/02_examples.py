"""
Topic: Chaining Functional Primitives vs Comprehensions
File: 02_examples.py
"""

def demonstrate_pipeline() -> None:
    prices = ["$12.50", "$99.00", "$5.99", "$45.00"]

    # Goal: Clean price strings to float, filter prices > $20, and sum total.

    # Option A: Map + Filter + Reduce
    from functools import reduce
    clean_floats = map(lambda p: float(p.replace("$", "")), prices)
    filtered = filter(lambda p: p > 20.0, clean_floats)
    total_functional = reduce(lambda a, b: a + b, filtered, 0.0)

    # Option B: Pythonic Generator Expression + Sum
    total_pythonic = sum(float(p.replace("$", "")) for p in prices if float(p.replace("$", "")) > 20.0)

    print(f"Functional Pipeline Total: ${total_functional:.2f}")
    print(f"Pythonic Generator Total:  ${total_pythonic:.2f}")


if __name__ == "__main__":
    demonstrate_pipeline()
