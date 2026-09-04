"""
Common Clean Code Violations and Anti-Patterns.
"""


def mistake_1_flag_arguments(data: list[int], sort_asc: bool, remove_negatives: bool) -> list[int]:
    """
    MISTAKE: Flag arguments (booleans passed as function arguments).
    WHY: Indicates the function is doing multiple things depending on the flag.
    Split into separate functions instead.
    """
    res = data.copy()
    if remove_negatives:
        res = [x for x in res if x >= 0]
    if sort_asc:
        res.sort()
    return res


def fix_1_separate_functions(data: list[int]) -> list[int]:
    """
    FIX: Keep functions focused on a single responsibility.
    Composing clean functions is clearer than passing flags.
    """
    return [x for x in data if x >= 0]


def mistake_2_magic_numbers(radius: float) -> float:
    """
    MISTAKE: Hardcoding magic numbers directly into business math.
    WHY: 3.14159 is hard to update or search for across codebase.
    """
    return 3.14159 * radius * radius


PI = 3.141592653589793


def fix_2_named_constants(radius: float) -> float:
    """
    FIX: Use named constant variables.
    """
    return PI * (radius ** 2)


if __name__ == "__main__":
    print("Executed clean code anti-patterns analysis.")
