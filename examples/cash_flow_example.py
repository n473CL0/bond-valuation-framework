# examples/cash_flow_example.py

from bonds.fixed_rate_bond import FixedRateBond
from interest_rate_models.constant_rate import ConstantRate
from utils.cash_flow import plot_cash_flows

# Define bond parameters
face_value = 1000
coupon_rate = 0.05
maturity = 5
payment_frequency = 2
interest_rate_model = ConstantRate(rate=0.03)

# Create a fixed-rate bond
bond = FixedRateBond(
    face_value=face_value,
    coupon_rate=coupon_rate,
    maturity=maturity,
    payment_frequency=payment_frequency,
    interest_rate_model=interest_rate_model
)

# Plot the cash flow diagram
plot_cash_flows(bond, title="Fixed-Rate Bond Cash Flows")