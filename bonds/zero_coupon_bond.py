from bonds.base_bond import Bond

class ZeroCouponBond(Bond):
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, price: float, maturity: float, inflation_model, tax_rate: float, payment_frequency: int):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param price: The current price of the bond.
        :param maturity: The time to maturity (in years).
        :param discount_rate_model: The discount rate model to use for cash flow calculations.
                                    Must implement a `get_discount_rates(times)` method.
        """
        super().__init__(face_value, price, maturity, inflation_model)
        self.tax_rate = tax_rate # tax rate in percent
        self.payment_frequency = payment_frequency
        self.ytm = (self.face_value / self.price) ** (1 / (self.maturity * self.payment_frequency)) - 1 # ytm as a float

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the bond.
        This method should be overridden by subclasses.

        :return: A list of tuples (time, cash_flow), where `time` is the time at which the cash flow occurs.
        """
        """
        Calculate the cash flows of the fixed-rate bond.

        :return: A list of tuples (time_period, cash_flow).
        """
        cash_flows = [(0, -self.price)]
        n_periods = int(self.maturity * self.payment_frequency)


        taxable_income = 0

        for t in range(1, n_periods):
            taxable_income += (1 + self.ytm) ** (t - 1)

        taxable_income *= self.ytm * self.price

        # Add face value repayment and final coupon payment at maturity
        cash_flows.append((self.maturity, taxable_income + self.face_value))

        return cash_flows

