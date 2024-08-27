# Calculator
from art import logo


# Add
def add(n1, n2):
    """Adds 2 numbers together."""
    return (n1 + n2)


# Subtract
def subtract(n1, n2):
    """Subtracts the second number from the first."""
    return (n1 - n2)


# Multiply
def multiply(n1, n2):
    """Multiplies the 2 numbers."""
    return (n1 * n2)


# Divide
def divide(n1, n2):
    """Divides the first number by the second."""
    return (n1 / n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    another_operation = True
    num1 = float(input(" What is the first number?: "))
    for symbol in operations:
        print(symbol)

    while another_operation:
        operation_symbol = input("Select an operation: ")
        num2 = float(input(" What is the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        any_more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if any_more != "y":
            another_operation = False
            calculator()
        else:
            num1 = answer


calculator()