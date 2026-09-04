"""
Solutions: Design Patterns Exercises.
"""

from typing import Protocol


class TargetPrinter(Protocol):
    def print_text(self, text: str) -> None:
        ...


class OldPrinter:
    def legacy_print(self, msg: str) -> None:
        print(f"OLD: {msg}")


class OldPrinterAdapter:
    def __init__(self, old: OldPrinter) -> None:
        self.old = old

    def print_text(self, text: str) -> None:
        self.old.legacy_print(text)


def create_printer_adapter(old_printer: OldPrinter) -> TargetPrinter:
    return OldPrinterAdapter(old_printer)


class StrategyInterface(Protocol):
    def format(self, text: str) -> str:
        ...


class UpperCaseStrategy:
    def format(self, text: str) -> str:
        return text.upper()


def apply_formatting_strategy(strategy: StrategyInterface, text: str) -> str:
    return strategy.format(text)


if __name__ == "__main__":
    adapter = create_printer_adapter(OldPrinter())
    adapter.print_text("Testing adapter pattern")
    
    formatted = apply_formatting_strategy(UpperCaseStrategy(), "hello world")
    print("Formatted text:", formatted)
