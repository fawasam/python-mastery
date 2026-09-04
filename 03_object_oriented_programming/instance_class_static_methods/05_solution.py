"""
Topic: Method Types Solutions
File: 05_solution.py
"""

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return round(c * 1.8 + 32, 2)


class Counter:
    total_count: int = 0

    @classmethod
    def increment(cls) -> int:
        cls.total_count += 1
        return cls.total_count


class StringUtil:
    @staticmethod
    def clean_whitespace(s: str) -> str:
        return " ".join(s.split())

    @staticmethod
    def to_slug(s: str) -> str:
        clean = StringUtil.clean_whitespace(s).lower()
        return "-".join(clean.split())


class PaymentProcessor:
    supported_currencies = ["USD", "EUR", "GBP"]

    def __init__(self, merchant_id: str) -> None:
        self.merchant_id = merchant_id

    def process_payment(self, amount: float, currency: str) -> str:
        if currency not in self.supported_currencies:
            raise ValueError(f"Unsupported currency: {currency}")
        return f"Merchant {self.merchant_id}: Processed {self.format_currency(amount, currency)}"

    @classmethod
    def get_supported_currencies(cls) -> list[str]:
        return cls.supported_currencies.copy()

    @staticmethod
    def format_currency(amount: float, currency: str) -> str:
        return f"{currency} {amount:,.2f}"


if __name__ == "__main__":
    print("--- Level 1 ---")
    print(f"20°C -> {TemperatureConverter.celsius_to_fahrenheit(20.0)}°F")

    print("\n--- Level 2 ---")
    Counter.increment()
    Counter.increment()
    print(f"Total counter: {Counter.total_count}")

    print("\n--- Level 3 ---")
    print(f"Slug: '{StringUtil.to_slug('  Python  Mastery  Course  ')}'")

    print("\n--- Level 4 ---")
    processor = PaymentProcessor("MERCH_882")
    receipt = processor.process_payment(150.0, "USD")
    print(f"Receipt: {receipt}")
