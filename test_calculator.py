"""Unit tests for the Calculator class.

This module contains tests for all arithmetic operations provided
by the Calculator class, including addition, subtraction, multiplication,
division, and handling division by zero.
"""

import pytest
from calculator import Calculator


def test_sum():
    """Verify that the sum method returns the correct result."""
    calculator = Calculator(5, 4)
    assert calculator.sum() == 9


def test_subtract():
    """Verify that the subtract method returns the correct result."""
    calculator = Calculator(7, 2)
    assert calculator.subtract() == 5


def test_multiply():
    """Verify that the multiply method returns the correct result."""
    calculator = Calculator(3, 4)
    assert calculator.multiply() == 12


def test_divide():
    """Verify that the divide method returns the correct result."""
    calculator = Calculator(5, 2)
    assert calculator.divide() == pytest.approx(2.5, 0.00001)


def test_divide_by_zero():
    """Verify that divide raises ValueError when dividing by zero."""
    calculator = Calculator(5, 0)
    with pytest.raises(ValueError):
        calculator.divide()
