"""
Reentrant Lock (RLock) for Recursive/Nested Thread Operations.
"""

import threading


class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance
        # RLock permits the SAME thread to acquire lock multiple times recursively!
        self._lock = threading.RLock()

    def deposit(self, amount: float) -> None:
        with self._lock:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        with self._lock:
            if self.balance < amount:
                raise ValueError("Insufficient balance")
            self.balance -= amount

    def transfer(self, target_account: "BankAccount", amount: float) -> None:
        # Acquires self._lock, then calls withdraw() which ALSO attempts to acquire self._lock!
        # Standard Lock would DEADLOCK here; RLock succeeds seamlessly!
        with self._lock:
            self.withdraw(amount)
            target_account.deposit(amount)


if __name__ == "__main__":
    acc1 = BankAccount(100.0)
    acc2 = BankAccount(50.0)

    acc1.transfer(acc2, 30.0)
    assert acc1.balance == 70.0
    assert acc2.balance == 80.0
    print(f"RLock transfer complete: acc1=${acc1.balance}, acc2=${acc2.balance}")
