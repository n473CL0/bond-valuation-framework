import csv

from bonds.fixed_rate_bond import FixedRateBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel
from inflation_models.linear_inflation_model import LinearInflationModel
from inflation_models.vasicek_inflation_model import VasicekDiscountRateModel


FILEPATH = '_data/csv/'

def get_inflation_models():

    constant_i = ConstantDiscountRateModel(rate=0.02)
    linear_i = LinearInflationModel(initial_rate=0.01, rate_change_per_year=0.004)

    return [None, constant_i, linear_i]


def get_profit_data(bond, inflation_models, step=0.005, steps=8):
    
    coupon_rates = [t * step for t in range(steps)]
    profit_data = [coupon_rates]

    for im in inflation_models:
        bond.inflation_model = im
        profits = []
        for cr in coupon_rates:
            bond.coupon_rate = cr
            profits.append(bond.profit(present_value=True))
        profit_data.append(profits)

    return profit_data


def save_profit_data(profit_data, headers, filename):

    # Write to CSV file
    with open(FILEPATH + filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(headers)

        # Write the data rows
        writer.writerows(zip(*profit_data))

def main():

    bond = FixedRateBond(
        face_value=1000,
        price=900,
        maturity=5,
        payment_frequency=2,
        coupon_rate=0,
        inflation_model=None
    )

    inflation_models = get_inflation_models()
    profit_data = get_profit_data(bond, inflation_models)
    headers = ['CouponRate', 'None', 'Constant', 'Linear']

    print(profit_data)

    save_profit_data(profit_data, headers, 'fix-rate.csv')

main()