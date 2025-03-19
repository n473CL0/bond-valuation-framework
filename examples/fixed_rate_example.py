# examples/fixed_rate_example.py

from bonds.fixed_rate_bond import FixedRateBond
from interest_rate_models.constant_rate import ConstantRate

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

# Calculate and print the bond price
price = bond.calculate_price()
print(f"Bond Price: ${price:.2f}")

# Calculate and print the yield to maturity (YTM)
market_price = 1086.98
ytm = bond.calculate_yield(market_price)
print(f"Yield to Maturity (YTM): {ytm * 100:.2f}%")

# Adjust for inflation
inflation_rate = 0.02  # 2% inflation
real_value = bond.adjust_for_inflation(inflation_rate)
print(f"Bond Face Value (Real): ${real_value:.2f}")