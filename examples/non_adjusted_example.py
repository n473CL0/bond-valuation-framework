from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel

# Create a constant discount rate model
constant_discount_model = ConstantDiscountRateModel(rate=0.05)

# Create a fixed-rate bond
bond = FixedRateBond(
    face_value=1000,
    price=1010,
    coupon_rate=0.05,  # 5% annual coupon rate
    maturity=5,  # 5 years to maturity
    payment_frequency=2,  # Semi-annual payments (2 per year)
    inflation_model=constant_discount_model
)

# Plot cash flows
bond.plot_cash_flows(title="Non-Inflation-Adjusted Bond Cash Flows")