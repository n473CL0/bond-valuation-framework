import numpy as np

class ReferenceRateFunction:
    """
    Base class for reference rate functions.
    Subclasses should implement the `get_rate` method.
    """

    def get_rate(self, time: float) -> float:
        """
        Get the reference rate at a given time.

        :param time: The time at which to calculate the reference rate.
        :return: The reference rate at the given time.
        """
        raise NotImplementedError("Subclasses must implement get_rate().")


class ConstantReferenceRate(ReferenceRateFunction):
    """
    A reference rate function that returns a constant rate.
    """

    def __init__(self, rate: float):
        """
        Initialize the constant reference rate function.

        :param rate: The constant reference rate.
        """
        self.rate = rate

    def get_rate(self, time: float) -> float:
        """
        Get the constant reference rate.

        :param time: The time at which to calculate the reference rate (ignored for constant rate).
        :return: The constant reference rate.
        """
        return self.rate


class LinearReferenceRate(ReferenceRateFunction):
    """
    A reference rate function that changes linearly over time.
    """

    def __init__(self, initial_rate: float, rate_change_per_year: float):
        """
        Initialize the linear reference rate function.

        :param initial_rate: The initial reference rate at time 0.
        :param rate_change_per_year: The constant change in the reference rate per year.
        """
        self.initial_rate = initial_rate
        self.rate_change_per_year = rate_change_per_year

    def get_rate(self, time: float) -> float:
        """
        Get the reference rate at a given time.

        :param time: The time at which to calculate the reference rate.
        :return: The reference rate at the given time.
        """
        return self.initial_rate + self.rate_change_per_year * time