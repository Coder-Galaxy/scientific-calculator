import unittest
from cal import (
    calculate_sqrt,
    calculate_factorial,
    calculate_log,
    calculate_power
)


class TestScientificCalculator(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(calculate_sqrt(25), 5.0)

    def test_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_log(self):
        self.assertAlmostEqual(calculate_log(10), 2.30258509299, places=5)

    def test_power(self):
        self.assertEqual(calculate_power(2, 3), 8.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calculate_sqrt(-4)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            calculate_log(0)


if __name__ == "__main__":
    unittest.main()

