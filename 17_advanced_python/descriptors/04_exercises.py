"""
Exercises: Building Descriptor Classes.
"""

from typing import Any


class StringTypeDescriptor:
    """
    Exercise: Implement descriptor enforcing that assigned attribute values are strings.
    
    Level 1 - Easy
    """
    def __set_name__(self, owner: type, name: str) -> None:
        raise NotImplementedError

    def __get__(self, instance: Any, owner: type) -> Any:
        raise NotImplementedError

    def __set__(self, instance: Any, value: Any) -> None:
        raise NotImplementedError
