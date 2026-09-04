"""
Topic: Common Mistakes with Lambda Functions
File: 03_common_mistakes.py
"""

def mistake_1_assigning_lambda_to_variable() -> None:
    # ❌ DISCOURAGED (PEP 8): f = lambda x: x * 2
    # Standard PEP 8 rule: Always use a def statement instead of assigning a lambda to a variable name!
    
    # ✅ CORRECT: Use def for reusable named functions
    def double(x: int) -> int:
        return x * 2

    print(f"PEP 8 compliant function call: {double(5)}")


def mistake_2_late_binding_in_closures() -> None:
    # ❌ TRAP: Lambdas created inside loops bind to variable names, NOT value snapshots!
    funcs = [lambda: i for i in range(3)]
    results = [f() for f in funcs]
    print(f"Late binding result (all evaluate to 2!): {results}")

    # ✅ CORRECT: Bind default parameter snapshot `i=i`
    fixed_funcs = [lambda i=i: i for i in range(3)]
    fixed_results = [f() for f in fixed_funcs]
    print(f"Default arg snapshot result:              {fixed_results}")


if __name__ == "__main__":
    mistake_1_assigning_lambda_to_variable()
    mistake_2_late_binding_in_closures()
