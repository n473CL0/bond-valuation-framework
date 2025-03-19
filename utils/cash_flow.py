# utils/cash_flow.py

import matplotlib.pyplot as plt

def plot_cash_flows(bond, title="Bond Cash Flow Diagram"):
    """
    Plot the cash flow diagram for a bond using a bar chart.

    :param bond: The bond object (must have calculate_cash_flows() method).
    :param title: The title of the plot.
    """
    # Get the cash flows from the bond
    cash_flows = bond.calculate_cash_flows()

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