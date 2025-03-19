from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.linear_inflation_model import LinearInflationModel

# Create a linear inflation model
linear_inflation_model = LinearInflationModel(
    initial_rate=0.03,  # Initial discount rate of 3%
    rate_change_per_year=0.01  # Discount rate increases by 1% per year
)

# Create a fixed-rate bond
bond = FixedRateBond(
    face_value=1000,  # Face value of the bond
    price=950,  # Current price of the bond
    coupon_rate=0.05,  # 5% annual coupon rate
    maturity=5,  # 5 years to maturity
    payment_frequency=2,  # Semi-annual payments (2 per year)
    inflation_model=linear_inflation_model  # Use the linear inflation model
)

# Get the bond data table
bond_data_table = bond.get_bond_data_table()

# Display the table
print("Bond Data Table with Linear Inflation Model:")
print(bond_data_table)

# Export the table to a CSV file
bond_data_table.to_csv("bond_data_linear_inflation.csv", index=False)
print("\nBond data exported to 'bond_data_linear_inflation.csv'.")