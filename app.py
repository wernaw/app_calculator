"""
Flask Calculator App.

Provides arithmetic operations via HTTP GET requests, including sum, subtract,
multiply, and divide. Includes input validation and error handling.
"""

from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)


@app.route("/")
def home():
    """Return a short instruction message for the calculator app."""
    return "This is a calculator app. Use /calculate?operation=...&arg1=...&arg2=..."


@app.route("/calculate")
def calculate():
    """Calculate the result of an arithmetic operation on two arguments.

    Supported operations: sum, subtract, multiply, divide.

    Parameters:
        operation: the operation to perform (sum, subtract, multiply, divide)
        arg1: first numeric argument
        arg2: second numeric argument

    Returns:
        The result of the operation as a string, or an error message with status 400.
    """
    operation = request.args.get("operation", type=str)
    try:
        arg1 = float(request.args.get("arg1", 0))
        arg2 = float(request.args.get("arg2", 0))
    except ValueError:
        return "Error: Arguments must be numeric.", 400

    available_operations = ["sum", "subtract", "multiply", "divide"]

    if not operation:
        return "Error: No operation provided.", 400

    if operation not in available_operations:
        return (
            f"Error: Invalid operation. Available operations are: "
            f"{', '.join(available_operations)}."
        ), 400

    if operation == "divide" and arg2 == 0:
        return "Error: Division by zero.", 400

    calculator = Calculator(arg1, arg2)

    operations_map = {
        "sum": calculator.sum,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
    }

    result = operations_map[operation]()
    return str(result)


if __name__ == "__main__":
    app.run()
