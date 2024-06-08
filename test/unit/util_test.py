import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())
        
    def test_validate_permissions(self):
        self.assertTrue(util.validate_permissions("operation", "user1"))
        self.assertFalse(util.validate_permissions("operation", "user2"))

    def test_invalid_convert_to_number(self):
        self.assertEqual(4, util.InvalidConvertToNumber("4"))
        self.assertEqual(0, util.InvalidConvertToNumber("0"))
        self.assertEqual(0, util.InvalidConvertToNumber("-0"))
        self.assertEqual(-1, util.InvalidConvertToNumber("-1"))
        self.assertAlmostEqual(4.0, util.InvalidConvertToNumber("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.InvalidConvertToNumber("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.InvalidConvertToNumber("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.InvalidConvertToNumber("-1.0"), delta=0.0000001)

    def test_convert_to_number_extreme_values(self):
        self.assertEqual(0.0, util.convert_to_number("1e-324"))
        self.assertEqual(0.0, util.convert_to_number("-1e-324"))

    def test_convert_to_number_boundary_values(self):
        self.assertEqual(9007199254740991, util.convert_to_number("9007199254740991"))  # Máximo valor de enteros de 64 bits
        self.assertEqual(9007199254740992.0, util.convert_to_number("9007199254740992"))  # Unidad más que el máximo valor de enteros de 64 bits
        self.assertEqual(-9007199254740991, util.convert_to_number("-9007199254740991"))  # Mínimo valor de enteros de 64 bits
        self.assertEqual(-9007199254740992.0, util.convert_to_number("-9007199254740992"))  # Unidad más que el mínimo valor de enteros de 64 bits

    def test_convert_to_number_different_formats(self):
        self.assertEqual(10, util.convert_to_number("0xa"))  # Número hexadecimal
        self.assertEqual(3.14159, util.convert_to_number("3.14159"))  # Número decimal
        self.assertEqual(1000.0, util.convert_to_number("1e3"))  # Notación científica
        self.assertEqual(1234567890, util.convert_to_number("1_234_567_890"))  # Separador de guiones bajos

if __name__ == '__main__':
    unittest.main()