# Floating Rate Note
from bonds.floating_rate_note import FloatingRateNote
from inflation_models.constant_inflation_model import ConstantDiscountRateModel


import os

# Filepath settings
graph_filepath = "_data/graph/"
table_filepath = "_data/csv/"

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
