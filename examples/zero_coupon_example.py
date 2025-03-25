from bonds.zero_coupon_bond import ZeroCouponBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel

inflation = ConstantDiscountRateModel(
    rate=0.015
)

zcb = ZeroCouponBond(
    face_value=4000,
    price=3600,
    maturity=5,
    payment_frequency=2,
    inflation_model=inflation,
    tax_rate=0.3
)

zcb.plot_cash_flows(title="Zero Coupon, Non-Inflation-Adjusted")

zcb.plot_cash_flows(title="Zero Coupon, Infaltion-Adjusted", inflation_adjusted=True)