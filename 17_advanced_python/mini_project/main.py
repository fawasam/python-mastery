"""
Advanced Python Mini Project: Metaclass, Descriptor & AST Engine.
"""

import ast
from typing import Any, Type


# 1. Custom Descriptor for Validated Fields
class FieldDescriptor:
    def __init__(self, field_type: Type[Any]) -> None:
        self.field_type = field_type

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, self.field_type):
            raise TypeError(f"Value '{value}' must be of type {self.field_type.__name__}")
        setattr(instance, self.storage_name, value)


# 2. Metaclass registering fields automatically
class ModelMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> Any:
        fields = {}
        for key, val in dct.items():
            if isinstance(val, FieldDescriptor):
                fields[key] = val
        dct["_fields"] = fields
        return super().__new__(cls, name, bases, dct)


class BaseModel(metaclass=ModelMeta):
    pass


class UserModel(BaseModel):
    username = FieldDescriptor(str)
    age = FieldDescriptor(int)

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age


# 3. AST Static Analysis
def audit_source_ast(code: str) -> bool:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            print(f"AST Inspected Class Definition: '{node.name}'")
    return True


def main() -> None:
    print("=== Advanced Python Framework Execution ===")
    user = UserModel(username="alice_dev", age=28)
    print(f"Instantiated UserModel: username={user.username}, age={user.age}")
    print("Registered model fields via Metaclass:", list(UserModel._fields.keys()))

    sample_code = "class SampleOrder:\n    pass"
    audit_source_ast(sample_code)


if __name__ == "__main__":
    main()
