import unittest
from calculator.operators import *


class TestOperators(unittest.TestCase):

    def setUp(self):
        self.add = Add(10, 10)
        self.subtract = Subtract(10, 10)
        self.multiply = Multiply(10, 10)
        self.divide = Divide(10, 10)
        self.factorial = Factorial()
        self.fibonacci = Fibonacci()

    def test_add(self):
        self.assertEqual(20, self.add.addition())

        self.add = Add(30, -50)

        self.assertEqual(-20, self.add.addition())

    def test_subtract(self):
        self.assertEqual(0, self.subtract.subtraction())

        self.subtract = Subtract(10, -10)

        self.assertEqual(20, self.subtract.subtraction())

    def test_multiply(self):
        self.assertEqual(100, self.multiply.multiplication())

        self.multiply = Multiply(10, -1)

        self.assertEqual(-10, self.multiply.multiplication())

    def test_divide(self):
        self.assertEqual(1, self.divide.division())

        self.divide = Divide(10, 0)

        with self.assertRaises(ValueError):
            self.divide.division()

    def test_factorial(self):
        self.assertEqual(120, self.factorial.factorial(5))

    def test_fibonacci(self):
        self.assertEqual(8, self.fibonacci.fibonacci(6))


if __name__ == '__main__':
    unittest.main()
