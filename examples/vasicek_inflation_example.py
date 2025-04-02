from bonds.fixed_rate_bond import FixedRateBond
from bonds.floating_rate_note import FloatingRateNote
from bonds.zero_coupon_bond import ZeroCouponBond
from bonds.partially_amortizing_bond import PartiallyAmortizingBond
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel

import os

# Filepath settings
graph_filepath = "_data/graph/"
table_filepath = "_data/csv/"

# Ensure directories exist
os.makedirs(graph_filepath, exist_ok=True)
os.makedirs(table_filepath, exist_ok=True)

# Create a Vasicek inflation model
inflation = VasicekDiscountRateModel(
    a=0.1,  # Mean reversion speed
    b=0.03,  # Long-term mean rate
    sigma=0.01,  # Volatility
    r0=0.02,  # Initial rate
    max_time=10,  # Maximum simulation time in years
    dt=0.25  # Quarterly time steps
)

# Common bond parameters
face_value = 1000
price = 900
maturity = 5
payment_frequency = 2  # Semi-annual

# Fixed Rate Bond
fix_rate = FixedRateBond(
    face_value=face_value,
    price=price,
    maturity=maturity,
    payment_frequency=payment_frequency,
    inflation_model=inflation,
    coupon_rate=0.05
)

fix_rate.plot_cash_flows("Fixed-rate cash flows - nominal", filepath=graph_filepath + "fix_nominal")
fix_rate.plot_cash_flows("Fixed-rate cash flows - adjusted for inflation", filepath=graph_filepath + "fix_inflation_adjusted", inflation_adjusted=True)
fix_rate.table_cash_flows().to_csv(table_filepath + "fixbon_coninfl.csv", index=False)

# Zero Coupon Bond
zero_coupon = ZeroCouponBond(
    face_value=face_value,
    price=price,
    maturity=maturity,
    payment_frequency=payment_frequency,
    inflation_model=inflation,
    tax_rate=0.3,
)

zero_coupon.plot_cash_flows("Zero-coupon cash flows - nominal", filepath=graph_filepath + "zero_nominal")
zero_coupon.plot_cash_flows("Zero-coupon cash flows - adjusted for inflation", filepath=graph_filepath + "zero_inflation_adjusted", inflation_adjusted=True)
zero_coupon.table_cash_flows().to_csv(table_filepath + "zero_coninfl.csv", index=False)

# Floating Rate Note
floating_rate = FloatingRateNote(
    face_value=face_value,
    price=price,
    maturity=maturity,
    payment_frequency=payment_frequency,
    spread_bps=2,  # Example spread of 2%
    inflation_model=inflation
)

floating_rate.plot_cash_flows("Floating-rate cash flows - nominal", filepath=graph_filepath + "float_nominal")
floating_rate.plot_cash_flows("Floating-rate cash flows - adjusted for inflation", filepath=graph_filepath + "float_inflation_adjusted", inflation_adjusted=True)
floating_rate.table_cash_flows().to_csv(table_filepath + "float_coninfl.csv", index=False)

# Partially Amortizing Bond
partially_amortizing = PartiallyAmortizingBond(
    face_value=face_value,
    price=price,
    maturity=maturity,
    payment_frequency=payment_frequency,
    coupon_rate=0.05,  # 5% coupon rate
    baloon_payment=500,  # Example baloon payment at the end
    inflation_model=inflation
)

partially_amortizing.plot_cash_flows("Partially amortizing cash flows - nominal", filepath=graph_filepath + "part_nominal")
partially_amortizing.plot_cash_flows("Partially amortizing cash flows - adjusted for inflation", filepath=graph_filepath + "part_inflation_adjusted", inflation_adjusted=True)
partially_amortizing.table_cash_flows().to_csv(table_filepath + "part_coninfl.csv", index=False)

for bond in [fix_rate, zero_coupon, floating_rate, partially_amortizing]:
    print(f'{bond.__class__.__name__} : profit {round(bond.profit(),2)}, interest adjusted {round(bond.profit(present_value=True),2)}')

print("All plots and tables have been generated successfully.")
