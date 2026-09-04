"""
Topic: Encapsulation Solutions
File: 05_solution.py
"""

class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        self.__balance = max(0.0, initial_balance)

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount


class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = 0.0
        self.set_celsius(celsius)

    def get_celsius(self) -> float:
        return self._celsius

    def set_celsius(self, val: float) -> None:
        if val < -273.15:
            raise ValueError("Temperature below absolute zero is invalid.")
        self._celsius = val


class APISession:
    def __init__(self, token: str) -> None:
        self.__token = token
        self.__is_active = True

    def get_token(self) -> str:
        if not self.__is_active:
            raise PermissionError("Session expired.")
        return self.__token

    def revoke(self) -> None:
        self.__is_active = False
        print("Session token revoked.")


if __name__ == "__main__":
    print("--- Level 1 ---")
    acc = BankAccount(100.0)
    acc.deposit(50.0)
    print(f"Balance: ${acc.get_balance()}")

    print("\n--- Level 2 ---")
    t = Temperature(25.0)
    print(f"Temperature: {t.get_celsius()}°C")

    print("\n--- Level 4 ---")
    session = APISession("bearer_token_xyz")
    print(f"Token: {session.get_token()}")
    session.revoke()
