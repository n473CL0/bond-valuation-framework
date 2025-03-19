# interest_rate_models/constant_rate.py

class ConstantRate:
    """
    A class representing a constant interest rate model.
    """

    def __init__(self, rate: float):
        """
        Initialize the constant interest rate model.

        :param rate: The constant annual interest rate (e.g., 0.03 for 3%).
        """
        self.rate = rate

    def get_rate(self) -> float:
        """
        Get the constant interest rate.

        :return: The constant annual interest rate.
        """
        return self.rate