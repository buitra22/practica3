import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(0, self.calc.sqrt(0))
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_log10_method_returns_correct_result(self):
        self.assertAlmostEqual(2, self.calc.log10(100), delta=0.000001)
        with self.assertRaises(ValueError):
            self.calc.log10(0)
        with self.assertRaises(ValueError):
            self.calc.log10(-1)

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(4, self.calc.subtract(6, 2))
        self.assertEqual(-4, self.calc.subtract(2, 6))
        self.assertEqual(1, self.calc.subtract(3, 2))
        self.assertEqual(-1, self.calc.subtract(2, 3))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0, self.calc.power(0, 5))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_log10_method_fails_with_non_positive_number(self):
        with self.assertRaises(ValueError):
            self.calc.log10(0)
        with self.assertRaises(ValueError):
            self.calc.log10(-1)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    @patch('app.util.validate_permissions', return_value=False)
    def test_multiply_method_fails_with_invalid_permissions(self, _validate_permissions):
        with self.assertRaises(InvalidPermissions):
            self.calc.multiply(2, 2)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
