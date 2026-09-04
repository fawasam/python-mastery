"""
Topic: Variables & Memory References
File: 02_examples.py

Demonstrates advanced variable features:
- Tuple unpacking for variable assignment
- Swapping variables idiomatically
- Memory address inspection using id()
"""

def demonstrate_variable_unpacking() -> None:
    # 1. Multiple assignment (Unpacking)
    # Assigning multiple variables in a single clean line
    host, port, protocol = "localhost", 8080, "https"
    print(f"Connecting to {protocol}://{host}:{port}")

    # 2. Variable Swapping
    # Python allows swapping values without a temp variable!
    # Under the hood, Python creates a temporary tuple (b, a) and unpacks it into a, b.
    a = 100
    b = 500
    print(f"\nBefore swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap:  a={a}, b={b}")

    # 3. Inspecting Memory IDs
    # id() returns the unique memory identity of the object the variable references.
    val1 = "Python"
    val2 = "Python"
    # Small string interning makes both variables point to the exact same memory address!
    print(f"\nMemory address of val1: {id(val1)}")
    print(f"Memory address of val2: {id(val2)}")
    print(f"Do they reference the exact same object? {val1 is val2}")


if __name__ == "__main__":
    demonstrate_variable_unpacking()
