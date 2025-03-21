from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel


# Create a partially amortizing bond
bond = FixedRateBond(
    face_value=300000000,  # Face value of the bond
    price=301000000,  # Current price of the bond
    maturity=5,  # 5 years to maturity
    inflation_model=None,  # Use the constant discount rate model
    coupon_rate=0.032,  # 3.2% annual coupon rate
    payment_frequency=2,  # Semi-annual payments (2 per year)
)

# Plot cash flows and discount rates
bond.plot_cash_flows(filepath="_data/graphs/", inflation_adjusted=False)