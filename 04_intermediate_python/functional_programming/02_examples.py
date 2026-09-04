"""
Topic: Function Composition Example
File: 02_examples.py
"""
from typing import Callable, TypeVar

T = TypeVar("T")

def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose multiple single-argument functions left-to-right."""
    def result(x: Any) -> Any:
        for f in functions:
            x = f(x)
        return x
    return result


if __name__ == "__main__":
    from typing import Any

    strip_str = lambda s: s.strip()
    lowercase = lambda s: s.lower()
    slugify = lambda s: s.replace(" ", "-")

    clean_pipeline = compose(strip_str, lowercase, slugify)

    raw_title = "  Python Functional Architecture  "
    print(f"Original: '{raw_title}'")
    print(f"Pipeline: '{clean_pipeline(raw_title)}'")
