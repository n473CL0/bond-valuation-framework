import unittest
from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel
from inflation_models.linear_inflation_model import LinearInflationModel

class TestFixedRateBond(unittest.TestCase):
    def setUp(self):
        # Create a fixed-rate bond for testing
        self.face_value = 1000
        self.price = 950
        self.coupon_rate = 0.05
        self.maturity = 5
        self.payment_frequency = 2

        # Create inflation models for testing
        self.constant_model = ConstantDiscountRateModel(rate=0.05)
        self.vasicek_model = VasicekDiscountRateModel(a=0.1, b=0.05, sigma=0.02, r0=0.03, max_time=5)
        self.linear_model = LinearInflationModel(initial_rate=0.03, rate_change_per_year=0.01)

    def test_calculate_cash_flows(self):
        # Test cash flow calculation with constant discount rate
        bond = FixedRateBond(
            face_value=self.face_value,
            price=self.price,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            inflation_model=self.constant_model
        )

        cash_flows = bond.calculate_cash_flows()
        self.assertEqual(len(cash_flows), 11)  # 10 coupon payments + 1 final payment
        self.assertEqual(cash_flows[0], (0, -950))  # Initial investment
        self.assertEqual(cash_flows[-1], (5, 1025))  # Final payment (face value + last coupon)

    def test_calculate_pv_of_cash_flows_constant_model(self):
        # Test present value calculation with constant discount rate
        bond = FixedRateBond(
            face_value=self.face_value,
            price=self.price,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            inflation_model=self.constant_model
        )

        pv_cash_flows = bond.calculate_pv_of_cash_flows()
        self.assertEqual(len(pv_cash_flows), 11)  # 10 coupon payments + 1 final payment
        self.assertAlmostEqual(pv_cash_flows[0][1], -950, places=2)  # Initial investment (no discounting)
        self.assertAlmostEqual(pv_cash_flows[-1][1], 803.11, places=2)  # Final payment discounted

    def test_calculate_pv_of_cash_flows_vasicek_model(self):
        # Test present value calculation with Vasicek discount rate
        bond = FixedRateBond(
            face_value=self.face_value,
            price=self.price,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            inflation_model=self.vasicek_model
        )

        pv_cash_flows = bond.calculate_pv_of_cash_flows()
        self.assertEqual(len(pv_cash_flows), 11)  # 10 coupon payments + 1 final payment
        self.assertAlmostEqual(pv_cash_flows[0][1], -950, places=2)  # Initial investment (no discounting)

    def test_calculate_pv_of_cash_flows_linear_model(self):
        # Test present value calculation with linear inflation model
        bond = FixedRateBond(
            face_value=self.face_value,
            price=self.price,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            inflation_model=self.linear_model
        )

        pv_cash_flows = bond.calculate_pv_of_cash_flows()
        self.assertEqual(len(pv_cash_flows), 11)  # 10 coupon payments + 1 final payment
        self.assertAlmostEqual(pv_cash_flows[0][1], -950, places=2)  # Initial investment (no discounting)

    def test_get_bond_data_table(self):
        # Test bond data table generation
        bond = FixedRateBond(
            face_value=self.face_value,
            price=self.price,
            coupon_rate=self.coupon_rate,
            maturity=self.maturity,
            payment_frequency=self.payment_frequency,
            inflation_model=self.constant_model
        )

        bond_data_table = bond.table_cash_flows()
        self.assertEqual(len(bond_data_table), 11)  # 10 coupon payments + 1 final payment
        self.assertEqual(bond_data_table.columns.tolist(), [
            "Time (Years)", "Nominal Cash Flow", "Real Cash Flow", "Real Net Cash", "Discount Rate"
        ])

if __name__ == "__main__":
    unittest.main()