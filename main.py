# Floating Rate Note
import csv
from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel


import os

# Filepath settings
graph_filepath = "_data/graph/"
table_filepath = "_data/csv/coupon_adjustments"

# Ensure directories exist
os.makedirs(graph_filepath, exist_ok=True)
os.makedirs(table_filepath, exist_ok=True)


# Create a constant inflation model
inflation = ConstantDiscountRateModel(rate=0.03)

# Common bond parameters
face_value = 1000
price = 900
maturity = 5
payment_frequency = 2  # Semi-annual

bond = FixedRateBond(
    face_value=face_value,
    price=price,
    maturity=maturity,
    coupon_rate=0,
    payment_frequency=payment_frequency,
    inflation_model=inflation
)

coupon_rates = []
nominal_profits = []
constant_profits = []
linear_profits = []



for cr in range(8):
    coupon_rates.append(cr * 0.005)
    bond.coupon_rate = coupon_rates[-1]
    profits.append(bond.profit())
    profits_pv.append(bond.profit(present_value=True))

filename = 'fix_rate_cp_vary.csv'

headers = ["Coupon Rate", "Profit", "Profit (PV)"]
rows = zip(coupon_rates, profits, profits_pv)

# Write to CSV file
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers
    writer.writerow(headers)

    # Write the data rows
    writer.writerows(rows)
