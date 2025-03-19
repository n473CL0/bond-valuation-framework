# bonds/fixed_rate_bond.py

from bonds.base_bond import Bond

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
        :param interest_rate_model: The interest rate model to use for cash flow calculations.
        """
        super().__init__(face_value, maturity, interest_rate_model)
        self.coupon_rate = coupon_rate
        self.payment_frequency = payment_frequency

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the fixed-rate bond.

        :return: A list of tuples (time_period, cash_flow).
        """
        cash_flows = []
        n_periods = int(self.maturity * self.payment_frequency)
        coupon_payment = (self.coupon_rate / self.payment_frequency) * self.face_value

        for t in range(1, n_periods):
            time_period = t / self.payment_frequency
            cash_flows.append((time_period, coupon_payment))

        # Add face value repayment and final coupon payment at maturity
        cash_flows.append((self.maturity, self.face_value + coupon_payment))

        return cash_flows