# interest_rate_models/time_varying_rate.py

class TimeVaryingRate:
    """
    A class representing a time-varying interest rate model.
    """

    def __init__(self, initial_rate: float, rate_change_per_year: float):
        """
        Initialize the time-varying interest rate model.

        :param initial_rate: The initial annual interest rate (e.g., 0.03 for 3%).
        :param rate_change_per_year: The annual change in the interest rate (e.g., 0.01 for 1% increase per year).
        """
        self.initial_rate = initial_rate
        self.rate_change_per_year = rate_change_per_year

    def get_rate(self, time: float) -> float:
        """
        Get the interest rate at a specific time.

        :param time: The time in years.
        :return: The annual interest rate at the given time.
        """
        return self.initial_rate + self.rate_change_per_year * time