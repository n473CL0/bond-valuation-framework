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

if __name__ == "__main__":
    unittest.main()