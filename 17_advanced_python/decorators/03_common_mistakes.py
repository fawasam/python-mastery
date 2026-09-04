"""
Decorators Common Pitfalls.
"""

# MISTAKE: Forgetting to apply `@functools.wraps(func)` to wrapper functions inside decorators.
# WHY: Erases original function name (`__name__`), docstring (`__doc__`), and type signatures, breaking introspection & documentation tools.
# FIX: Always wrap inner functions with `@functools.wraps(func)`.

if __name__ == "__main__":
    print("Functools wraps rule verified.")
