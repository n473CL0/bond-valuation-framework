class ConstantDiscountRateModel:
    """
    A discount rate model with a constant discount rate.
    """

    def __init__(self, rate: float):
        """
        Initialize the model with a constant discount rate.

        :param rate: The constant discount rate.
        """
        self.rate = rate

    def get_discount_rates(self, times: list) -> list:
        """
        Return a list of constant discount rates for the given times.

        :param times: A list of times at which the discount rates are requested.
        :return: A list of constant discount rates.
        """
        return [self.rate for _ in times]