# tests/test_interest_rate_models.py

import unittest
from interest_rate_models.constant_rate import ConstantRate
from interest_rate_models.time_varying_rate import TimeVaryingRate

class TestConstantRate(unittest.TestCase):
    """
    Unit tests for the ConstantRate class.
    """

    def test_initialization(self):
        """
        Test that the ConstantRate class initializes correctly.
        """
        rate = 0.03
        model = ConstantRate(rate)
        self.assertEqual(model.get_rate(), rate)

    def test_get_rate(self):
        """
        Test the get_rate() method.
        """
        rate = 0.03
        model = ConstantRate(rate)
        self.assertEqual(model.get_rate(), rate)

class TestTimeVaryingRate(unittest.TestCase):
    """
    Unit tests for the TimeVaryingRate class.
    """

    def test_initialization(self):
        """
        Test that the TimeVaryingRate class initializes correctly.
        """
        initial_rate = 0.03
        rate_change_per_year = 0.01
        model = TimeVaryingRate(initial_rate, rate_change_per_year)
        self.assertEqual(model.initial_rate, initial_rate)
        self.assertEqual(model.rate_change_per_year, rate_change_per_year)

    def test_get_rate(self):
        """
        Test the get_rate() method.
        """
        initial_rate = 0.03
        rate_change_per_year = 0.01
        model = TimeVaryingRate(initial_rate, rate_change_per_year)

        # Test at time = 0
        self.assertEqual(model.get_rate(0), initial_rate)

        # Test at time = 1
        self.assertEqual(model.get_rate(1), initial_rate + rate_change_per_year)

        # Test at time = 5
        self.assertEqual(model.get_rate(5), initial_rate + 5 * rate_change_per_year)

if __name__ == "__main__":
    unittest.main()