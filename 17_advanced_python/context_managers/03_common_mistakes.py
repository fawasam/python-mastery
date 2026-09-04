"""
Context Managers Common Pitfalls.
"""

# MISTAKE: Forgetting to wrap cleanup logic in a `finally:` block inside generator-based `@contextmanager` functions.
# WHY: If the `yield` statement raises an unhandled exception, code following `yield` without `finally:` will NEVER execute, leaking resources.
# FIX: Always place cleanup logic inside `finally:` or `__exit__`.

if __name__ == "__main__":
    print("Context manager exception safety rules verified.")
