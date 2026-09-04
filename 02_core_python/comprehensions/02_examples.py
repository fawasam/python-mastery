"""
Topic: Flattening Matrix with Nested Comprehension
File: 02_examples.py
"""

def demonstrate_matrix_flattening() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # Nested List Comprehension syntax reads in outer-to-inner loop order:
    # `for row in matrix` -> `for val in row`
    flattened = [val for row in matrix for val in row if val % 2 == 0]
    print(f"Original Matrix: {matrix}")
    print(f"Flattened Evens: {flattened}")


if __name__ == "__main__":
    demonstrate_matrix_flattening()
