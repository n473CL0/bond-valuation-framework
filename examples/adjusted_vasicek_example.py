from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel

# Create a Vasicek discount rate model
vasicek_discount_model = VasicekDiscountRateModel(
    a=0.1,  # Speed of mean reversion
    b=0.05,  # Long-term mean rate
    sigma=0.02,  # Volatility
    r0=0.03,  # Initial discount rate
    max_time=5  # Maximum time for simulation
)

# Create a fixed-rate bond
bond = FixedRateBond(
    face_value=1000,
    price=950,
    coupon_rate=0.05,  # 5% annual coupon rate
    maturity=5,  # 5 years to maturity
    payment_frequency=2,  # Semi-annual payments (2 per year)
    inflation_model=vasicek_discount_model
)

# Plot inflation-adjusted cash flows
bond.plot_cash_flows(title="Inflation-Adjusted Bond Cash Flows", inflation_adjusted=True)