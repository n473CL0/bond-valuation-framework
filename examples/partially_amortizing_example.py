from bonds.partially_amortizing_bond import PartiallyAmortizingBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel

# Create a partially amortizing bond
bond = PartiallyAmortizingBond(
    face_value=3000,  # Face value of the bond
    price=3020,  # Current price of the bond
    maturity=5,  # 5 years to maturity
    inflation_model=None,  # Use the constant discount rate model
    coupon_rate=0.032,  # 3.2% annual coupon rate
    payment_frequency=2,  # Semi-annual payments (2 per year)
    baloon_payment=1500  # Balloon payment at maturity
)

# Plot cash flows and discount rates
bond.plot_cash_flows(filepath="_data/graphs/", inflation_adjusted=False)