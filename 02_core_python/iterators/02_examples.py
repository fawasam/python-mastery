"""
Topic: Custom Iterator Class Implementation
File: 02_examples.py
"""

class FibonacciIterator:
    """Custom iterator yielding Fibonacci numbers up to limit count."""
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> "FibonacciIterator":
        return self

    def __next__(self) -> int:
        if self.count >= self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val


if __name__ == "__main__":
    print("First 8 Fibonacci numbers via custom iterator:")
    fib_gen = FibonacciIterator(8)
    for num in fib_gen:
        print(num, end=" ")
    print()
