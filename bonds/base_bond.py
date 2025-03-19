import matplotlib.pyplot as plt
import pandas as pd

class Bond:
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, price: float, maturity: float, inflation_model):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param price: The current price of the bond.
        :param maturity: The time to maturity (in years).
        :param discount_rate_model: The discount rate model to use for cash flow calculations.
                                    Must implement a `get_discount_rates(times)` method.
        """
        self.face_value = face_value
        self.price = price
        self.maturity = maturity
        self.inflation_model = inflation_model

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the bond.
        This method should be overridden by subclasses.

        :return: A list of tuples (time, cash_flow), where `time` is the time at which the cash flow occurs.
        """
        raise NotImplementedError("Subclasses must implement calculate_cash_flows().")

    def calculate_pv_of_cash_flows(self) -> list:
        """
        Calculate the present value of the bond's cash flows using the discount rate model.

        :return: A list of tuples (time, present_value), where `time` is the time at which the cash flow occurs.
        """
        cash_flows = self.calculate_cash_flows()
        times = [time for time, _ in cash_flows]  # Extract times from cash flows
        discount_rates = self.inflation_model.get_discount_rates(times)  # Get discount rates for all times

        present_values = [
            (time, cash_flow * (1 + discount_rate) ** (-time))
            for (time, cash_flow), discount_rate in zip(cash_flows, discount_rates)
        ]
        return present_values
    
    def plot_cash_flows(bond, title="Bond Cash Flow Diagram", inflation_adjusted=False):
        """
        Plot the cash flow diagram for a bond using a bar chart.
        If inflation_adjusted is True, also plot the discount rate on a separate subplot.
        Overlay the cumulative sum of cash flows on the cash flow subplot.

        :param bond: The bond object.
        :param title: The title of the plot.
        :param inflation_adjusted: Whether to plot inflation-adjusted cash flows and discount rates.
        """
        if inflation_adjusted:
            cash_flows = bond.calculate_pv_of_cash_flows()
        else:
            cash_flows = bond.calculate_cash_flows()

        times = [cf[0] for cf in cash_flows]
        amounts = [cf[1] for cf in cash_flows]

        # Calculate cumulative sum of cash flows
        cumulative_cash_flows = [sum(amounts[:i+1]) for i in range(len(amounts))]

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))  # Smaller figure size
        fig.suptitle(title, fontsize=14)

        # Plot cash flows on the first subplot
        bars = ax1.bar(times, amounts, width=0.4, color='blue', alpha=0.7, label="Cash Flows")
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=8)

        # Overlay cumulative cash flows as a line graph
        ax1.plot(times, cumulative_cash_flows, color='green', marker='o', label="Cumulative Cash Flows")
        ax1.axhline(0, color='black', linewidth=0.8)
        ax1.set_xlabel("Time (Years)", fontsize=10)
        ax1.set_ylabel("Cash Flow Amount ($)", fontsize=10)
        ax1.grid(True, linestyle='--', alpha=0.6)
        ax1.set_xticks(times)
        ax1.set_title("Cash Flows and Cumulative Cash Flows", fontsize=12)
        ax1.legend(loc="upper left")

        # Plot discount rates on the second subplot if inflation_adjusted is True
        if inflation_adjusted:
            discount_rates = bond.inflation_model.get_discount_rates(times)
            ax2.plot(times, discount_rates, color='red', marker='o', label="Discount Rate")
            ax2.set_xlabel("Time (Years)", fontsize=10)
            ax2.set_ylabel("Discount Rate (%)", color='red', fontsize=10)
            ax2.tick_params(axis='y', labelcolor='red')
            ax2.grid(True, linestyle='--', alpha=0.6)
            ax2.set_title("Discount Rates Over Time", fontsize=12)

        # Add bond parameters as text outside the figure
        params_label = (
            f"Face Value: ${bond.face_value:.2f}\n"
            f"Coupon Rate: {bond.coupon_rate * 100:.2f}%\n"
            f"Maturity: {bond.maturity} years\n"
            f"Payment Frequency: {bond.payment_frequency} per year"
        )
        plt.figtext(
            0.95, 0.5, params_label, fontsize=10,
            verticalalignment='center', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.5')
        )

        # Adjust layout and display
        plt.tight_layout()
        plt.subplots_adjust(right=0.7)  # Make space for the text box
        plt.show()

    def get_bond_data_table(self) -> pd.DataFrame:
        """
        Create a DataFrame with the bond's cash flow data, including:
        - Time (Years)
        - Nominal Cash Flow
        - Real Cash Flow (Inflation-Adjusted)
        - Cumulative Sum of Real Cash Flows
        - Discount Rate at Each Payment Time

        :return: A pandas DataFrame containing the bond data.
        """
        # Calculate nominal and real cash flows
        nominal_cash_flows = self.calculate_cash_flows()
        real_cash_flows = self.calculate_pv_of_cash_flows()

        # Extract times, nominal amounts, and real amounts
        times = [cf[0] for cf in nominal_cash_flows]
        nominal_amounts = [cf[1] for cf in nominal_cash_flows]
        real_amounts = [cf[1] for cf in real_cash_flows]

        # Calculate cumulative sum of real cash flows
        cumulative_real_amounts = [sum(real_amounts[:i+1]) for i in range(len(real_amounts))]

        # Get discount rates at each payment time
        discount_rates = self.inflation_model.get_discount_rates(times)

        # Create a DataFrame
        data = {
            "Time (Years)": times,
            "Nominal Cash Flow": nominal_amounts,
            "Real Cash Flow": real_amounts,
            "Real Net Cash": cumulative_real_amounts,
            "Discount Rate": discount_rates
        }
        df = pd.DataFrame(data)

        return df