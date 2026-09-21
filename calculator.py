import math


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def modulus(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulus by zero.")
        return a % b

    def floor_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform floor division by zero.")
        return a // b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(a)

    def absolute(self, a):
        return abs(a)

    def factorial(self, a):
        if a < 0 or not float(a).is_integer():
            raise ValueError("Factorial requires a non-negative integer.")
        return math.factorial(int(a))

    def percentage(self, value, percent):
        return (value * percent) / 100