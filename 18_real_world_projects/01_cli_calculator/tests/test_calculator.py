"""
Unit Tests for Calculator Engine.
"""

import pytest
from app.calculator import CalculatorEngine


def test_calculator_add() -> None:
    assert CalculatorEngine.add(5.0, 3.0) == 8.0


def test_calculator_divide_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        CalculatorEngine.divide(10.0, 0.0)
