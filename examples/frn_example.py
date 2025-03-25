from bonds.floating_rate_note import FloatingRateNote
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel


inflation = VasicekDiscountRateModel(
    a=0.1,  # Speed of mean reversion
    b=0.05,  # Long-term mean rate
    sigma=0.02,  # Volatility
    r0=0.03,  # Initial discount rate
    max_time=3  # Maximum time for simulation
)

frn = FloatingRateNote(
    face_value=10000,
    price=11000,
    maturity=3,
    payment_frequency=2,
    inflation_model=inflation,
    spread_bps=130,
)

frn.plot_cash_flows(title="Floating Rate Note Nominal Cash Flow", inflation_adjusted=True)