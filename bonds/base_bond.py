# bonds/base_bond.py

import matplotlib.pyplot as plt

class Bond:
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, maturity: float, interest_rate_model):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param maturity: The time to maturity (in years).
        :param interest_rate_model: The interest rate model to use for cash flow calculations.
        """
        self.face_value = face_value
        self.maturity = maturity
        self.interest_rate_model = interest_rate_model

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the bond.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement calculate_cash_flows().")

    def calculate_present_value(self) -> float:
        """
        Calculate the present value of the bond's cash flows using the interest rate model.

        :return: The present value of the bond.
        """
        cash_flows = self.calculate_cash_flows()
        present_value = 0.0

        for time, cash_flow in cash_flows:
            rate = self.interest_rate_model.get_rate(time)
            discount_factor = (1 + rate) ** (-time)
            present_value += cash_flow * discount_factor

        return present_value

    def plot_cash_flows(self, title="Bond Cash Flow Diagram"):
        """
        Plot the cash flow diagram for a bond using a bar chart.

        :param bond: The bond object (must have calculate_cash_flows() method).
        :param title: The title of the plot.
        """
        # Get the cash flows from the bond
        cash_flows = self.calculate_cash_flows()

        # Extract time periods and amounts
        times = [cf[0] for cf in cash_flows]
        amounts = [cf[1] for cf in cash_flows]

        # Sum the final coupon payment and face value repayment
        if len(times) > 1:
            times[-1] = times[-1]  # Ensure the last time is correct

        # Create the plot
        plt.figure(figsize=(12, 6))
        bars = plt.bar(times, amounts, width=0.4, color='blue', alpha=0.7)

        # Add labels to each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                    f'{height:.2f}', ha='center', va='bottom')

        # Add a horizontal line at y=0
        plt.axhline(0, color='black', linewidth=0.8)

        # Customize the plot
        plt.title(title)
        plt.xlabel("Time (Years)")
        plt.ylabel("Cash Flow Amount ($)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(times)  # Ensure x-ticks align with the bars
        plt.show()