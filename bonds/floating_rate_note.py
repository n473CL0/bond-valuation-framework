from bonds.base_bond import Bond

class FloatingRateNote(Bond):
    """
    A class representing a floating rate note (FRN).
    The coupon rate of an FRN is not fixed but fluctuates based on a reference interest rate.
    """

    def __init__(self, face_value: float, price: float, maturity: float, payment_frequency: int, reference_rate_function, inflation_model):
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
        self.reference_rate_function = reference_rate_function

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the floating rate note.
        The coupon payments are based on the reference rate at each payment time.

        :return: A list of tuples (time, cash_flow), where `time` is the time at which the cash flow occurs.
        """
        raise NotImplementedError("This will be where Cici's code goes")