from bonds.base_bond import Bond

class PartiallyAmortizingBond(Bond):
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, price: float, maturity: float, inflation_model, coupon_rate: float, payment_frequency: int, baloon_payment: float):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param price: The current price of the bond.
        :param maturity: The time to maturity (in years).
        :param discount_rate_model: The discount rate model to use for cash flow calculations.
                                    Must implement a `get_discount_rates(times)` method.
        """
        super().__init__(face_value, payment_frequency, price, maturity, inflation_model)
        self.coupon_rate = coupon_rate
        self.baloon_payment = baloon_payment

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the fixed-rate bond.

        :return: A list of tuples (time_period, cash_flow).
        """
        cash_flows = [(0, -self.price)]
        n_periods = int(self.maturity * self.payment_frequency)
        r_period = (self.coupon_rate / self.payment_frequency)
        pv_baloon_payment = self.baloon_payment / (1 + r_period) ** n_periods 
        print(pv_baloon_payment)
        periodic_payment = (r_period * (self.face_value - pv_baloon_payment)) / (1 - (1 + r_period) ** -n_periods)
        print(periodic_payment)
                            
        for t in range(1, n_periods):
            time_period = t / self.payment_frequency
            cash_flows.append((time_period, periodic_payment))

        # Add face value repayment and final coupon payment at maturity
        final_payment = self.baloon_payment + periodic_payment
        cash_flows.append((self.maturity, final_payment))

        return cash_flows