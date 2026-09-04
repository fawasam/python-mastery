"""
Topic: Common Mistakes with Generators
File: 03_common_mistakes.py
"""

def mistake_1_expecting_return_value_from_generator() -> None:
    def gen_with_return():
        yield 1
        yield 2
        return "FINISHED"  # Value in 'return' becomes StopIteration.value!

    g = gen_with_return()
    print("Item:", next(g))
    print("Item:", next(g))
    try:
        next(g)
    except StopIteration as e:
        print(f"Generator return value attached to StopIteration exception: '{e.value}'")


if __name__ == "__main__":
    mistake_1_expecting_return_value_from_generator()
