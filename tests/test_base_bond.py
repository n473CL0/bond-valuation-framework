# tests/test_base_bond.py

import unittest
from bonds.base_bond import Bond

class TestBond(unittest.TestCase):
    """
    Unit tests for the base Bond class.
    """

    def test_initialization(self):
        """
        Test that the Bond class initializes correctly.
        """
        bond = Bond(face_value=1000, maturity=5, interest_rate_model=None)
        self.assertEqual(bond.face_value, 1000)
        self.assertEqual(bond.maturity, 5)
        self.assertIsNone(bond.interest_rate_model)

    def test_calculate_price_not_implemented(self):
        """
        Test that calculate_price() raises NotImplementedError.
        """
        bond = Bond(face_value=1000, maturity=5, interest_rate_model=None)
        with self.assertRaises(NotImplementedError):
            bond.calculate_price()

    def test_calculate_yield_not_implemented(self):
        """
        Test that calculate_yield() raises NotImplementedError.
        """
        bond = Bond(face_value=1000, maturity=5, interest_rate_model=None)
        with self.assertRaises(NotImplementedError):
            bond.calculate_yield()

    def test_adjust_for_inflation(self):
        """
        Test the adjust_for_inflation() method.
        """
        class MockBond(Bond):
            def calculate_price(self):
                return 1000  # Mock price for testing

        bond = MockBond(face_value=1000, maturity=5, interest_rate_model=None)
        real_value = bond.adjust_for_inflation(inflation_rate=0.02)
        self.assertAlmostEqual(real_value, 1000 / (1.02) ** 5, places=2)

if __name__ == "__main__":
    unittest.main()