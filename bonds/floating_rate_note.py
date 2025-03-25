from bonds.base_bond import Bond
from inflation_models.discount_rate_model import DiscountRateModel

class FloatingRateNote(Bond):
    """
    A class representing a floating rate note (FRN).
    The coupon rate of an FRN is not fixed but fluctuates based on a reference interest rate.
    """

    def __init__(self, face_value: float, price: float, maturity: float, payment_frequency: int, inflation_model: DiscountRateModel, spread_bps: int):
        """
        Initialize a floating rate note.

        :param face_value: The face value (principal) of the bond.
        :param price: The current price of the bond.
        :param maturity: The time to maturity (in years).
        :param payment_frequency: The number of coupon payments per year.
        :param reference_rate_function: A function that returns the reference rate at a given time.
        :param inflation_model: The inflation model to use for cash flow calculations.
        """
        super().__init__(face_value, price, maturity, inflation_model)
        self.payment_frequency = payment_frequency
        self.spread = spread_bps / 100

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the floating rate note.
        The coupon payments are based on the reference rate at each payment time.

        :return: A list of tuples (time, cash_flow), where `time` is the time at which the cash flow occurs.
        """
        cash_flows = [(0, -self.price)]
        n_periods = int(self.maturity * self.payment_frequency)
        
        times = [t / self.payment_frequency for t in range(1, n_periods)]

        for time_period, mrr in zip(times, self.inflation_model.get_discount_rates(times)):
            coupon_rate = self.spread + mrr
            coupon_payment = (coupon_rate / self.payment_frequency) * self.face_value

            cash_flows.append((time_period, coupon_payment))

        # Add face value repayment and final coupon payment at maturity
        final_payment = self.face_value + coupon_payment
        cash_flows.append((self.maturity, final_payment))

        return cash_flows