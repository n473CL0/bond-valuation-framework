import numpy as np
from inflation_models.discount_rate_model import DiscountRateModel

class VasicekDiscountRateModel(DiscountRateModel):
    """
    A discount rate model based on the Vasicek interest rate model.
    """

    def __init__(self, a: float, b: float, sigma: float, r0: float, max_time: float, dt: float = 0.25):
        """
        Initialize the Vasicek model.

        :param a: Speed of mean reversion.
        :param b: Long-term mean rate.
        :param sigma: Volatility of the rate.
        :param r0: Initial discount rate.
        :param max_time: The maximum time for which to simulate the discount rate path.
        :param dt: Time step for the simulation.
        """
        self.a = a
        self.b = b
        self.sigma = sigma
        self.r0 = r0
        self.max_time = max_time
        self.dt = dt
        self.times, self.discount_rates = self._simulate_vasicek_path()

    def _simulate_vasicek_path(self):
        """
        Simulate a single path of discount rates using the Vasicek model.

        :return: A tuple (times, discount_rates), where `times` is a list of time steps and
                 `discount_rates` is a list of corresponding discount rates.
        """
        n_steps = int(self.max_time / self.dt)
        times = np.arange(0, self.max_time + self.dt, self.dt)
        discount_rates = np.zeros(n_steps + 1)
        discount_rates[0] = self.r0

        for t in range(1, n_steps + 1):
            dr = self.a * (self.b - discount_rates[t - 1]) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal()
            discount_rates[t] = discount_rates[t - 1] + dr

        return times, discount_rates

    def get_discount_rates(self, times: list) -> list:
        """
        Return the discount rates at the specified times by interpolating the simulated path.

        :param times: A list of times at which the discount rates are requested.
        :return: A list of discount rates corresponding to the requested times.
        """
        return [np.interp(time, self.times, self.discount_rates) for time in times]