class LinearInflationModel:
    """
    An inflation model where the discount rate changes by a constant amount over time.
    """

    def __init__(self, initial_rate: float, rate_change_per_year: float):
        """
        Initialize the linear inflation model.

        :param initial_rate: The initial discount rate at time 0.
        :param rate_change_per_year: The constant change in the discount rate per year.
        """
        self.initial_rate = initial_rate
        self.rate_change_per_year = rate_change_per_year

    def get_discount_rates(self, times: list) -> list:
        """
        Calculate the discount rates at the given times.

        :param times: A list of times at which the discount rates are requested.
        :return: A list of discount rates corresponding to the given times.
        """
        return [self.initial_rate + self.rate_change_per_year * time for time in times]