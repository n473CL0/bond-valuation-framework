# bonds/fixed_rate_bond.py

from bonds.base_bond import Bond
import numpy as np

class FixedRateBond(Bond):
    """
    A class representing a fixed-rate bond.
    """

    def __init__(self, face_value: float, coupon_rate: float, maturity: float, payment_frequency: int, interest_rate_model):
        """
        Initialize a fixed-rate bond.

        :param face_value: The face value (principal) of the bond.
        :param coupon_rate: The annual coupon rate (e.g., 0.05 for 5%).
        :param maturity: The time to maturity (in years).
        :param payment_frequency: The number of coupon payments per year.
        :param interest_rate_model: The interest rate model to use for valuation.
        """
        super().__init__(face_value, maturity, interest_rate_model)
        self.coupon_rate = coupon_rate
        self.payment_frequency = payment_frequency

    def calculate_cash_flows(self):
        """
        Calculate the bond's cash flows.

        :return: A list of tuples (time, amount) representing the cash flows.
        """
        cash_flows = []
        n_periods = self.maturity * self.payment_frequency
        coupon_payment = (self.coupon_rate / self.payment_frequency) * self.face_value

        # Add coupon payments
        for t in range(1, n_periods + 1):
            time = t / self.payment_frequency
            cash_flows.append((time, coupon_payment))

        # Add face value repayment at maturity (sum with the last coupon payment)
        cash_flows[-1] = (cash_flows[-1][0], cash_flows[-1][1] + self.face_value)

        return cash_flows

    def calculate_price(self) -> float:
        """
        Calculate the present value (price) of the fixed-rate bond.

        :return: The bond price.
        """
        # Calculate the coupon payment per period
        coupon_payment = (self.coupon_rate / self.payment_frequency) * self.face_value

        # Calculate the number of payment periods
        n_periods = self.maturity * self.payment_frequency

        # Calculate the periodic interest rate (annual rate divided by payment frequency)
        rate_per_period = self.interest_rate_model.get_rate() / self.payment_frequency

        # Calculate the present value of coupon payments (annuity formula)
        pv_coupons = coupon_payment * (1 - (1 + rate_per_period) ** (-n_periods)) / rate_per_period

        # Calculate the present value of the face value (single cash flow formula)
        pv_face_value = self.face_value / (1 + rate_per_period) ** n_periods

        # Bond price is the sum of the present values
        return pv_coupons + pv_face_value

    def calculate_yield(self, market_price: float) -> float:
        """
        Calculate the yield to maturity (YTM) of the fixed-rate bond using numerical methods.

        :param market_price: The current market price of the bond.
        :return: The yield to maturity (annualized).
        """
        def ytm_function(y):
            # Recalculate bond price using the given yield
            rate_per_period = y / self.payment_frequency
            n_periods = self.maturity * self.payment_frequency
            coupon_payment = (self.coupon_rate / self.payment_frequency) * self.face_value

            # Handle the case where the rate is zero
            if rate_per_period == 0:
                pv_coupons = coupon_payment * n_periods
                pv_face_value = self.face_value
            else:
                pv_coupons = coupon_payment * (1 - (1 + rate_per_period) ** (-n_periods)) / rate_per_period
                pv_face_value = self.face_value / (1 + rate_per_period) ** n_periods

            return pv_coupons + pv_face_value - market_price

        # Initial guess for YTM
        ytm = self.coupon_rate  # Start with the coupon rate as an initial guess
        tolerance = 1e-6
        max_iterations = 1000

        for _ in range(max_iterations):
            # Calculate the bond price and its derivative at the current YTM
            price = ytm_function(ytm)
            derivative = (ytm_function(ytm + tolerance) - price) / tolerance

            # Update YTM using Newton-Raphson
            ytm -= price / derivative

            # Check for convergence
            if abs(price) < tolerance:
                break

        return ytm