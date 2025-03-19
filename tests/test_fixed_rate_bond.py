# tests/test_fixed_rate_bond.py

import unittest
from bonds.fixed_rate_bond import FixedRateBond
from interest_rate_models.constant_rate import ConstantRate

class TestFixedRateBond(unittest.TestCase):
    """
    Unit tests for the FixedRateBond class.
    """

    def setUp(self):
        """
        Set up a fixed-rate bond for testing.
        """
        self.face_value = 1000
        self.coupon_rate = 0.05
        self.maturity = 5
        self.payment_frequency = 2
        self.interest_rate_model = ConstantRate(rate=0.03)
        self.bond = FixedRateBond(
            face_value=self.face_value,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            interest_rate_model=self.interest_rate_model
        )

    def test_initialization(self):
        """
        Test that the FixedRateBond class initializes correctly.
        """
        self.assertEqual(self.bond.face_value, self.face_value)
        self.assertEqual(self.bond.coupon_rate, self.coupon_rate)
        self.assertEqual(self.bond.maturity, self.maturity)
        self.assertEqual(self.bond.payment_frequency, self.payment_frequency)
        self.assertEqual(self.bond.interest_rate_model.get_rate(), 0.03)

if __name__ == "__main__":
    unittest.main()