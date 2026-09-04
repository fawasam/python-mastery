"""
Basic Custom Exception Class in Python.
"""


class BankError(Exception):
    """Base exception for banking domain failures."""

    pass


class InsufficientFundsError(BankError):
    """Raised when an account withdrawal exceeds available balance."""

    def __init__(self, balance: float, amount: float) -> None:
        super().__init__(f"Cannot withdraw ${amount:.2f}: Current balance is ${balance:.2f}")
        self.balance = balance
        self.amount = amount


class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    account = BankAccount(100.0)

    try:
        account.withdraw(150.0)
    except InsufficientFundsError as err:
        print(f"Caught Custom Exception: {err}")
        print(f"Inspected Details -> Balance: ${err.balance}, Attempted Amount: ${err.amount}")
