"""
Common Mistakes in Debugging Python Code.
"""


# MISTAKE 1: Leaving breakpoint() statements in production code
def mistake_leftover_breakpoint(data: list[int]) -> int:
    total = sum(data)
    # breakpoint()  <-- Leftover breakpoint halts server processes in production!
    return total


# MISTAKE 2: Modifying state during debugger evaluation
# Calling mutating functions like list.pop() or dict.pop() while inspecting variables inside pdb
# alters runtime application state!


if __name__ == "__main__":
    res = mistake_leftover_breakpoint([1, 2, 3])
    print(f"Result: {res}")
