import unittest
from inflation_models.constant_inflation_model import ConstantDiscountRateModel
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel
from inflation_models.linear_inflation_model import LinearInflationModel

class TestInflationModels(unittest.TestCase):
    def test_constant_discount_rate_model(self):
        # Test constant discount rate model
        model = ConstantDiscountRateModel(rate=0.05)
        times = [0, 1, 2, 3]
        discount_rates = model.get_discount_rates(times)
        self.assertEqual(discount_rates, [0.05, 0.05, 0.05, 0.05])

    def test_vasicek_discount_rate_model(self):
        # Test Vasicek discount rate model
        model = VasicekDiscountRateModel(a=0.1, b=0.05, sigma=0.02, r0=0.03, max_time=5)
        times = [0, 1, 2, 3]
        discount_rates = model.get_discount_rates(times)
        self.assertEqual(len(discount_rates), len(times))  # Ensure rates are returned for all times

    def test_linear_inflation_model(self):
        # Test linear inflation model
        model = LinearInflationModel(initial_rate=0.03, rate_change_per_year=0.01)
        times = [0, 1, 2, 3]
        discount_rates = model.get_discount_rates(times)
        self.assertEqual(discount_rates, [0.03, 0.04, 0.05, 0.06])

if __name__ == "__main__":
    unittest.main()