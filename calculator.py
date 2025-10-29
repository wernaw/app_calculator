"""
This module provides the Calculator class, which offers basic arithmetic functionality
such as addition, subtraction, multiplication, and division.
"""


class Calculator:
    """
    Perform basic arithmetic operations.
    """

    def __init__(self, op1: float, op2: float):
        self._op1 = op1
        self._op2 = op2

    def sum(self) -> float:
        """Return the sum of the two operands."""
        return self._op1 + self._op2

    def subtract(self) -> float:
        """Return the difference of the two operands."""
        return self._op1 - self._op2

    def multiply(self) -> float:
        """Return the product of the two operands."""
        return self._op1 * self._op2

    def divide(self) -> float:
        """Return the quotient of the two operands."""
        if self._op2 == 0:
            raise ValueError("Division by zero.")
        return self._op1 / self._op2
