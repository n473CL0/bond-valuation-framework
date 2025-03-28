from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel

# Create a constant discount rate model
constant_discount_model = ConstantDiscountRateModel(rate=0.05)  # 5% constant discount rate

# Create a fixed-rate bond
bond = FixedRateBond(
    face_value=1000,  # Face value of the bond
    price=950,  # Current price of the bond
    coupon_rate=0.05,  # 5% annual coupon rate
    maturity=5,  # 5 years to maturity
    payment_frequency=2,  # Semi-annual payments (2 per year)
    inflation_model=constant_discount_model  # Use the constant discount rate model
)

# Get the bond data table
bond_data_table = bond.table_cash_flows()

# Display the table
print("Bond Data Table:")
print(bond_data_table)

# Export the table to a CSV file
bond_data_table.to_csv("examples/csv/bond_data.csv", index=False)
print("\nBond data exported to 'bond_data.csv'.")