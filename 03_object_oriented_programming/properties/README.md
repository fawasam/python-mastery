# Topic: Properties (`@property`, `@setter`, `@deleter`)

## What You Will Learn
- Pythonic attribute getters using `@property`.
- Attribute setters using `@property_name.setter` for validation and encapsulation.
- Attribute deleters using `@property_name.deleter`.
- Computed / derived properties.

## Syntax
```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, val: float) -> None:
        if val < -273.15:
            raise ValueError("Invalid temperature below absolute zero.")
        self._celsius = val

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 1.8 + 32
```

## Next Topic
Next: `composition` — "Has-A" composition relationships vs "Is-A" inheritance.
