"""
Solutions: Modular Design Exercises.
"""


def define_module_exports() -> list[str]:
    """
    Return explicitly exported public symbols.
    """
    return ["PublicService", "PublicConfig"]


if __name__ == "__main__":
    print("Module exports:", define_module_exports())
