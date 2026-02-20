import unittest
import math
from cal import (
    calculate_sqrt,
    calculate_factorial,
    calculate_log,
    calculate_power
)


class TestSquareRoot(unittest.TestCase):
    """Test cases for calculate_sqrt()"""

    # --- Valid inputs ---
    def test_sqrt_perfect_square(self):
        self.assertEqual(calculate_sqrt(25), 5.0)

    def test_sqrt_perfect_square_large(self):
        self.assertEqual(calculate_sqrt(10000), 100.0)

    def test_sqrt_zero(self):
        self.assertEqual(calculate_sqrt(0), 0.0)

    def test_sqrt_one(self):
        self.assertEqual(calculate_sqrt(1), 1.0)

    def test_sqrt_float(self):
        self.assertAlmostEqual(calculate_sqrt(2.0), 1.41421356, places=5)

    def test_sqrt_small_fraction(self):
        self.assertAlmostEqual(calculate_sqrt(0.25), 0.5, places=5)

    def test_sqrt_large_number(self):
        self.assertAlmostEqual(calculate_sqrt(1e10), 1e5, places=2)

    def test_sqrt_small_positive(self):
        self.assertAlmostEqual(calculate_sqrt(0.0001), 0.01, places=5)

    def test_sqrt_9(self):
        self.assertEqual(calculate_sqrt(9), 3.0)

    def test_sqrt_144(self):
        self.assertEqual(calculate_sqrt(144), 12.0)

    def test_sqrt_return_type(self):
        result = calculate_sqrt(16)
        self.assertIsInstance(result, float)

    # --- Invalid / edge inputs ---
    def test_sqrt_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_sqrt(-1)

    def test_sqrt_negative_large_raises(self):
        with self.assertRaises(ValueError):
            calculate_sqrt(-100)

    def test_sqrt_negative_float_raises(self):
        with self.assertRaises(ValueError):
            calculate_sqrt(-0.5)


class TestFactorial(unittest.TestCase):
    """Test cases for calculate_factorial()"""

    # --- Valid inputs ---
    def test_factorial_zero(self):
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(calculate_factorial(1), 1)

    def test_factorial_five(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_factorial_ten(self):
        self.assertEqual(calculate_factorial(10), 3628800)

    def test_factorial_twelve(self):
        self.assertEqual(calculate_factorial(12), 479001600)

    def test_factorial_two(self):
        self.assertEqual(calculate_factorial(2), 2)

    def test_factorial_three(self):
        self.assertEqual(calculate_factorial(3), 6)

    def test_factorial_four(self):
        self.assertEqual(calculate_factorial(4), 24)

    def test_factorial_seven(self):
        self.assertEqual(calculate_factorial(7), 5040)

    def test_factorial_fifteen(self):
        self.assertEqual(calculate_factorial(15), 1307674368000)

    def test_factorial_twenty(self):
        self.assertEqual(calculate_factorial(20), 2432902008176640000)

    def test_factorial_return_type(self):
        result = calculate_factorial(5)
        self.assertIsInstance(result, int)

    # --- Invalid / edge inputs ---
    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    def test_factorial_negative_large_raises(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-10)


class TestNaturalLog(unittest.TestCase):
    """Test cases for calculate_log()"""

    # --- Valid inputs ---
    def test_log_of_one(self):
        self.assertAlmostEqual(calculate_log(1), 0.0, places=5)

    def test_log_of_e(self):
        self.assertAlmostEqual(calculate_log(math.e), 1.0, places=5)

    def test_log_of_ten(self):
        self.assertAlmostEqual(calculate_log(10), 2.302585, places=5)

    def test_log_of_hundred(self):
        self.assertAlmostEqual(calculate_log(100), 4.605170, places=5)

    def test_log_of_half(self):
        self.assertAlmostEqual(calculate_log(0.5), -0.693147, places=5)

    def test_log_of_two(self):
        self.assertAlmostEqual(calculate_log(2), 0.693147, places=5)

    def test_log_small_positive(self):
        self.assertAlmostEqual(calculate_log(0.0001), math.log(0.0001), places=5)

    def test_log_large_number(self):
        self.assertAlmostEqual(calculate_log(1e6), math.log(1e6), places=5)

    def test_log_return_type(self):
        result = calculate_log(5)
        self.assertIsInstance(result, float)

    # --- Invalid / edge inputs ---
    def test_log_zero_raises(self):
        with self.assertRaises(ValueError):
            calculate_log(0)

    def test_log_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_log(-5)

    def test_log_negative_float_raises(self):
        with self.assertRaises(ValueError):
            calculate_log(-0.001)


class TestPower(unittest.TestCase):
    """Test cases for calculate_power()"""

    # --- Valid inputs ---
    def test_power_basic(self):
        self.assertEqual(calculate_power(2, 3), 8.0)

    def test_power_zero_exponent(self):
        self.assertEqual(calculate_power(5, 0), 1.0)

    def test_power_one_base(self):
        self.assertEqual(calculate_power(1, 100), 1.0)

    def test_power_zero_base(self):
        self.assertEqual(calculate_power(0, 5), 0.0)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(calculate_power(2, -1), 0.5, places=5)

    def test_power_negative_base_even_exp(self):
        self.assertAlmostEqual(calculate_power(-2, 2), 4.0, places=5)

    def test_power_negative_base_odd_exp(self):
        self.assertAlmostEqual(calculate_power(-2, 3), -8.0, places=5)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(calculate_power(27, 1/3), 3.0, places=5)

    def test_power_float_base(self):
        self.assertAlmostEqual(calculate_power(2.5, 2), 6.25, places=5)

    def test_power_large(self):
        self.assertAlmostEqual(calculate_power(10, 6), 1e6, places=2)

    def test_power_square(self):
        self.assertEqual(calculate_power(7, 2), 49.0)

    def test_power_cube(self):
        self.assertEqual(calculate_power(3, 3), 27.0)

    def test_power_return_type(self):
        result = calculate_power(2, 3)
        self.assertIsInstance(result, float)

    def test_power_both_zero(self):
        # 0^0 is defined as 1.0 in Python's math.pow
        self.assertEqual(calculate_power(0, 0), 1.0)

    def test_power_fraction_base_fraction_exp(self):
        self.assertAlmostEqual(calculate_power(0.5, 0.5), math.pow(0.5, 0.5), places=8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
