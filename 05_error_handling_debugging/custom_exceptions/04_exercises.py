"""
Custom Exception Exercises.
"""


# Exercise 1 (Medium): Validation Exception Hierarchy
# Create a base exception ConfigError(Exception), and sub-exceptions:
# 1. MissingConfigKeyError(ConfigError) with key attribute
# 2. InvalidConfigValueError(ConfigError) with key and value attributes
class ConfigError(Exception):
    pass


class MissingConfigKeyError(ConfigError):
    def __init__(self, key: str) -> None:
        raise NotImplementedError("Implement MissingConfigKeyError")


class InvalidConfigValueError(ConfigError):
    def __init__(self, key: str, value: object) -> None:
        raise NotImplementedError("Implement InvalidConfigValueError")
