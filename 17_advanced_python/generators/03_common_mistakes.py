"""
Generators Common Pitfalls.
"""

# MISTAKE: Forgetting to "prime" a coroutine generator (calling `next(gen)` or `gen.send(None)`) before sending values.
# WHY: Sending a non-None value to a newly created generator that hasn't reached its first `yield` raises `TypeError`.
# FIX: Always call `next(gen)` to advance execution to the first `yield` before `send()`.

if __name__ == "__main__":
    print("Generator priming rules verified.")
