class DiscountRateModel:

    def __init__(self, rate: float):
        """
        Initialize the model with a constant discount rate.

        :param rate: The constant discount rate.
        """

    def get_discount_rates(self, times: list) -> list:
        """
        Calculate the discount rates at the given times.

        :param times: A list of times at which the discount rates are requested.
        :return: A list of discount rates corresponding to the given times.
        """
        raise NotImplementedError('Must be implemented by the subclass')