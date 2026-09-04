"""
Topic: Virtual Subclass Registration with ABC
File: 01_basic.py
"""
from abc import ABC, abstractmethod

class BaseDriver(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass


class ThirdPartyDriver:
    def connect(self) -> None:
        print("Connected via third-party driver.")


# Registering ThirdPartyDriver as a virtual subclass of BaseDriver
BaseDriver.register(ThirdPartyDriver)

if __name__ == "__main__":
    driver = ThirdPartyDriver()
    print(f"Is ThirdPartyDriver a subclass of BaseDriver? {issubclass(ThirdPartyDriver, BaseDriver)}")
    print(f"Is driver instance of BaseDriver?            {isinstance(driver, BaseDriver)}")
