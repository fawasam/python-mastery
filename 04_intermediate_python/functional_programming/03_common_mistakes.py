"""
Topic: Common Mistakes with Functional Programming
File: 03_common_mistakes.py
"""

def mistake_1_impure_functions_with_side_effects() -> None:
    global_cache = []

    # ❌ WRONG: Function relies on and mutates external state (Impure)!
    def add_impure(x: int) -> int:
        global_cache.append(x)  # Side effect!
        return x * 2

    # ✅ CORRECT: Pure functions return output determined SOLELY by input arguments without side-effects!
    print("Pure functions guarantee referential transparency (same input -> same output, no side-effects).")


if __name__ == "__main__":
    mistake_1_impure_functions_with_side_effects()
