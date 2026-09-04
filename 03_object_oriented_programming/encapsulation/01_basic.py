"""
Topic: Access Modifiers & Name Mangling
File: 01_basic.py
"""

class SecureVault:
    def __init__(self, owner: str, secret_code: str) -> None:
        self.owner = owner            # Public
        self._internal_log = []       # Protected
        self.__secret_code = secret_code # Strongly Private (Name Mangled)

    def verify_code(self, code: str) -> bool:
        return self.__secret_code == code


if __name__ == "__main__":
    vault = SecureVault("Alice", "9901")

    print(f"Public Owner: {vault.owner}")
    print(f"Verify code 9901: {vault.verify_code('9901')}")

    # Accessing name-mangled private attribute explicitly
    print(f"Name-mangled private attribute access: {vault._SecureVault__secret_code}")
