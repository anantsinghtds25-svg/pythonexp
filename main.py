import ast
import operator

from calculator import Calculator
from history import History
from utils import get_number, display_result, pause


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv
}


def evaluate_expression(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        return evaluate_node(tree.body)
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
        raise ValueError("Invalid mathematical expression.")


def evaluate_node(node):

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed.")

    if isinstance(node, ast.UnaryOp):
        operand = evaluate_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -operand

        if isinstance(node.op, ast.UAdd):
            return operand

        raise ValueError("Unsupported operator.")

    if isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator.")

        return operation(left, right)

    raise ValueError("Invalid expression.")


def basic_operations(calculator, history):
    while True:
        print("\n========== BASIC OPERATIONS ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Floor Division")
        print("7. Back")

        choice = input("\nEnter your choice: ")

        if choice == "7":
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice!")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = calculator.add(a, b)
                expression = f"{a} + {b}"

            elif choice == "2":
                result = calculator.subtract(a, b)
                expression = f"{a} - {b}"

            elif choice == "3":
                result = calculator.multiply(a, b)
                expression = f"{a} * {b}"

            elif choice == "4":
                result = calculator.divide(a, b)
                expression = f"{a} / {b}"

            elif choice == "5":
                result = calculator.modulus(a, b)
                expression = f"{a} % {b}"

            else:
                result = calculator.floor_divide(a, b)
                expression = f"{a} // {b}"

            display_result(result)
            history.add(expression, result)

        except ZeroDivisionError as error:
            print(f"Error: {error}")

        pause()


def advanced_operations(calculator, history):
    while True:
        print("\n========== ADVANCED OPERATIONS ==========")
        print("1. Power")
        print("2. Square Root")
        print("3. Absolute Value")
        print("4. Factorial")
        print("5. Percentage")
        print("6. Back")

        choice = input("\nEnter your choice: ")

        if choice == "6":
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice!")
            continue

        try:
            if choice == "1":
                a = get_number("Enter base: ")
                b = get_number("Enter power: ")

                result = calculator.power(a, b)
                expression = f"{a} ** {b}"

            elif choice == "2":
                a = get_number("Enter number: ")

                result = calculator.square_root(a)
                expression = f"√{a}"

            elif choice == "3":
                a = get_number("Enter number: ")

                result = calculator.absolute(a)
                expression = f"|{a}|"

            elif choice == "4":
                a = get_number("Enter a non-negative integer: ")

                result = calculator.factorial(a)
                expression = f"{int(a)}!"

            else:
                value = get_number("Enter value: ")
                percent = get_number("Enter percentage: ")

                result = calculator.percentage(value, percent)
                expression = f"{percent}% of {value}"

            display_result(result)
            history.add(expression, result)

        except ValueError as error:
            print(f"Error: {error}")

        pause()


def expression_calculator(history):
    print("\n========== EXPRESSION CALCULATOR ==========")
    print("Example: 25 + 5 * 2")
    print("Example: (100 + 50) / 5")
    print("Example: 2 ** 5")

    expression = input("\nEnter expression: ")

    try:
        result = evaluate_expression(expression)
        display_result(result)
        history.add(expression, result)

    except ValueError as error:
        print(f"Error: {error}")

    pause()


def main():
    calculator = Calculator()
    history = History()

    while True:
        print("\n")
        print("========================================")
        print("          PYTHON CALCULATOR")
        print("========================================")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Expression Calculator")
        print("4. View History")
        print("5. Clear History")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            basic_operations(calculator, history)

        elif choice == "2":
            advanced_operations(calculator, history)

        elif choice == "3":
            expression_calculator(history)

        elif choice == "4":
            history.display_history()
            pause()

        elif choice == "5":
            history.clear_history()
            pause()

        elif choice == "6":
            print("\nThank you for using Python Calculator!")
            break

        else:
            print("\nInvalid choice! Please select an option from 1-6.")


if __name__ == "__main__":
    main()