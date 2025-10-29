from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)


@app.route("/")
def home():
    return "This is calculator app. Use /calculate?operation=...&arg1=...&arg2=..."


@app.route("/calculate")
def calculate():
    """Calculate the result of an arithmetic operation on two arguments.

    Supported operations: sum, subtract, multiply, divide.

    Query Parameters:
    operation - the operation to perform (sum, subtract, multiply, divide)
    arg1 - first numeric argument
    arg2 - second numeric argument

    Returns:
    The result of the operation as a string, or an error message with status 400.
    """
    operation = request.args.get("operation",type=str)
    arg1 = float(request.args.get("arg1", type=int))
    arg2 = float(request.args.get("arg2", type=int))

    available_operations = ["sum", "subtract", "multiply", "divide"]

    if operation is None:
        return "Error: No operation provided", 400

    if operation not in ["sum", "subtract", "multiply", "divide"]:
        return (
            f"Error: Invalid operation. Available operations are: {', '.join(available_operations)}.",
            400,
        )

    if operation == "divide" and arg2 == 0:
        return "Error: Division by zero", 400

    calculator = Calculator(arg1, arg2)
    result = None

    if operation == "sum":
        result = calculator.sum()
    elif operation == "subtract":
        result = calculator.subtract()
    elif operation == "multiply":
        result = calculator.multiply()
    elif operation == "divide":
        result = calculator.divide()

    return str(result)


if __name__ == '__main__':
    app.run()
