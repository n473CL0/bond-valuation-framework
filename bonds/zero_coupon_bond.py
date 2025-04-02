from bonds.base_bond import Bond

import matplotlib.pyplot as plt
import os
import pandas as pd

class ZeroCouponBond(Bond):
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, price: float, maturity: float, inflation_model, tax_rate: float, payment_frequency: int):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param price: The current price of the bond.
        :param maturity: The time to maturity (in years).
        :param discount_rate_model: The discount rate model to use for cash flow calculations.
                                    Must implement a `get_discount_rates(times)` method.
        """
        super().__init__(face_value, payment_frequency, price, maturity, inflation_model)
        self.tax_rate = tax_rate # tax rate in percent
        self.ytm = (self.face_value / self.price) ** (1 / (self.maturity * self.payment_frequency)) - 1 # ytm as a float

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the bond.
        This method should be overridden by subclasses.

        :return: A list of tuples (time, cash_flow), where `time` is the time at which the cash flow occurs.
        """
        """
        Calculate the cash flows of the fixed-rate bond.

        :return: A list of tuples (time_period, cash_flow).
        """
        cash_flows = [(0, -self.price), (self.maturity, self.face_value)]

        return cash_flows
    
    def calculate_phantom_payments(self) -> list:
        phantom_payments = []
        n_periods = int(self.maturity * self.payment_frequency)
        
        for t in range(1, n_periods+1):
            cash_flow = self.ytm * self.price * (1 + self.ytm) ** (t - 1)
            phantom_payments.append((t / self.payment_frequency, cash_flow))

        return phantom_payments
    
    def calculate_pv_of_phantom_payments(self):
        phantom_payments = self.calculate_phantom_payments()
        times = [time for time, _ in phantom_payments]  # Extract times from cash flows
        discount_rates = self.inflation_model.get_discount_rates(times)  # Get discount rates for all times

        # Compute the cumulative discount factor over time
        cumulative_discount_factors = [1]  # Start with 1 for time = 0
        for i in range(1, len(discount_rates)):
            cumulative_discount_factors.append(cumulative_discount_factors[-1] * (1 + discount_rates[i]) ** -1)

        # Apply discounting correctly
        present_values = [
            (time, cash_flow * cumulative_discount_factor)
            for (time, cash_flow), cumulative_discount_factor in zip(phantom_payments, cumulative_discount_factors)
        ]

        return present_values

    
    def plot_cash_flows(bond, title="Cash Flows", filepath="_data/graphs/", inflation_adjusted=False):
        """
        Plot the cash flow diagram for a bond and save the plots to separate files.

        :param bond: The bond object.
        :param filepath: The directory where the plots will be saved (default: '_data/graphs/').
        :param inflation_adjusted: Whether to plot inflation-adjusted cash flows and discount rates.
        """
        if inflation_adjusted:
            cash_flows = bond.calculate_pv_of_cash_flows()
            phantom_flows = bond.calculate_pv_of_phantom_payments()
        else:
            cash_flows = bond.calculate_cash_flows()
            phantom_flows = bond.calculate_phantom_payments()

        print(cash_flows)

        times = [cf[0] for cf in cash_flows]
        amounts = [round(cf[1], 2) for cf in cash_flows]
        phantom_times = [ph[0] for ph in phantom_flows]
        phantom = [round(ph[1], 2) for ph in phantom_flows]

        # Create the directory if it doesn't exist
        os.makedirs(filepath, exist_ok=True)
        
        # Generate the base filename
        if inflation_adjusted:
            filename_base = f"{bond.__class__.__name__[:5]}-{bond.inflation_model.__class__.__name__[:5]}-{bond.face_value}"
        else:
            filename_base = f"{bond.__class__.__name__[:5]}-not_adjusted-{bond.face_value}"

        # Plot cash flows and cumulative sum
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        bars = ax1.bar(times, amounts, width=0.4, color='blue', alpha=0.7, label="Cash Flows")
        red_bars = ax1.bar(phantom_times, phantom, width=0.4, color='red', alpha=0.7, label="Phantom Payments")
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=8)
        for bar in red_bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=8)


        ax1.axhline(0, color='black', linewidth=0.8)
        ax1.set_xlabel("Time (Years)", fontsize=10)
        ax1.set_ylabel("Cash Flow Amount (£)", fontsize=10)
        ax1.grid(True, linestyle='--', alpha=0.6)
        ax1.set_xticks(times)
        ax1.set_title(title, fontsize=12)
        ax1.legend(loc="upper left")

        # Save the cash flow plot
        cash_flow_filename = os.path.join(filepath, f"{filename_base}-cash_flows.png")
        fig1.savefig(cash_flow_filename)
        plt.close(fig1)

        # Plot discount rates if inflation_adjusted is True
        if inflation_adjusted:
            discount_rates = bond.inflation_model.get_discount_rates(times)
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            ax2.plot(times, discount_rates, color='red', marker='o', label="Discount Rate")
            ax2.set_xlabel("Time (Years)", fontsize=10)
            ax2.set_ylabel("Discount Rate (%)", color='red', fontsize=10)
            ax2.tick_params(axis='y', labelcolor='red')
            ax2.grid(True, linestyle='--', alpha=0.6)
            ax2.set_title("Discount Rates Over Time", fontsize=12)

            # Save the discount rate plot
            discount_rate_filename = os.path.join(filepath, f"{filename_base}-discount_rates.png")
            fig2.savefig(discount_rate_filename)
            plt.close(fig2)

