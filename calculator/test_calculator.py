from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(3, 4), 7)

    def test_subtract(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.subtract(3, 4), -1)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.divide(12, 4), 3)
        self.assertEqual(self.calculator.divide(12, 0), 'Division by 0 not allowed!')

    def test_toPower(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.toPower(8, 2), 64)