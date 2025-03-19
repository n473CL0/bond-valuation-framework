# tests/test_inflation_adjustment.py

import unittest
from bonds.base_bond import Bond
from interest_rate_models.constant_rate import ConstantRate

class TestInflationAdjustment(unittest.TestCase):
    """
    Unit tests for inflation adjustment logic.
    """

    def setUp(self):
        """
        Set up a bond for testing.
        """
        self.face_value = 1000
        self.maturity = 5
        self.interest_rate_model = ConstantRate(rate=0.03)
        self.bond = Bond(
            face_value=self.face_value,
            maturity=self.maturity,
            interest_rate_model=self.interest_rate_model
        )

    def test_adjust_for_inflation(self):
        """
        Test the adjust_for_inflation() method.
        """
        inflation_rate = 0.02  # 2% inflation
        real_value = self.bond.adjust_for_inflation(inflation_rate)
        expected_real_value = 1000 / (1 + 0.02) ** 5
        self.assertAlmostEqual(real_value, expected_real_value, places=2)

    def test_adjust_for_inflation_zero_inflation(self):
        """
        Test the adjust_for_inflation() method when inflation is zero.
        """
        inflation_rate = 0.0  # 0% inflation
        real_value = self.bond.adjust_for_inflation(inflation_rate)
        self.assertAlmostEqual(real_value, self.face_value, places=2)

    def test_adjust_for_inflation_high_inflation(self):
        """
        Test the adjust_for_inflation() method with high inflation.
        """
        inflation_rate = 0.10  # 10% inflation
        real_value = self.bond