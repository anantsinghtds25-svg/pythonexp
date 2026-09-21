import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    def test_modulus(self):
        self.assertEqual(self.calculator.modulus(10, 3), 1)

    def test_floor_division(self):
        self.assertEqual(self.calculator.floor_divide(10, 3), 3)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 5), 32)

    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(25), 5)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_percentage(self):
        self.assertEqual(self.calculator.percentage(200, 10), 20)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()