import unittest
from src.calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_complex_calculation(self):
        # Simulating a more complex calculation workflow
        # (2 + 3) * 4 - 6
        result = self.calc.add(2, 3)  # 5
        result = self.calc.multiply(result, 4)  # 20
        result = self.calc.subtract(result, 6)  # 14
        self.assertEqual(result, 14)

    def test_division_chain(self):
        # Testing a chain of divisions
        # 100 / 2 / 5 = 10
        result = self.calc.divide(100, 2)  # 50
        result = self.calc.divide(result, 5)  # 10
        self.assertEqual(result, 10)

    def test_mixed_operations(self):
        # Testing a mix of operations
        # (10 * 2 + 5) - 15 = 10
        result = self.calc.multiply(10, 2)  # 20
        result = self.calc.add(result, 5)  # 25
        result = self.calc.subtract(result, 15)  # 10
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()