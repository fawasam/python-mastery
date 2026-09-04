"""
Basic Python Garbage Collection and Cycle Detection.
"""

import gc


class CircularNode:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ref = None

    def __repr__(self) -> str:
        return f"<CircularNode {self.name}>"


def demonstrate_cycle_cleanup() -> None:
    # Enable garbage collection tracking
    gc.enable()

    # Create two nodes with a circular reference loop
    node_a = CircularNode("A")
    node_b = CircularNode("B")
    node_a.ref = node_b
    node_b.ref = node_a

    # Remove local strong references from caller scope
    del node_a
    del node_b

    # Force a manual garbage collection pass
    unreachable_count = gc.collect()
    print(f"Garbage collection collected {unreachable_count} unreachable cyclic objects.")


if __name__ == "__main__":
    print(f"GC Enabled status: {gc.isenabled()}")
    print(f"Current GC thresholds (Gen0, Gen1, Gen2): {gc.get_threshold()}")

    print("\n--- Running Cycle Cleanup Demo ---")
    demonstrate_cycle_cleanup()
