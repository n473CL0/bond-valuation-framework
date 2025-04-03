import csv
from itertools import product

from bonds.fixed_rate_bond import FixedRateBond
from bonds.floating_rate_note import FloatingRateNote
from bonds.partially_amortizing_bond import PartiallyAmortizingBond
from bonds.zero_coupon_bond import ZeroCouponBond
from inflation_models.constant_inflation_model import ConstantDiscountRateModel
from inflation_models.linear_inflation_model import LinearInflationModel


FILEPATH = '_data/csv/'

# Common bond parameters
face_value = 1000
price = 900
maturity = 5
payment_frequency = 2  # Semi-annual


def get_inflation_models():

    constant_i = ConstantDiscountRateModel(rate=0.02)
    linear_i = LinearInflationModel(initial_rate=0.01, rate_change_per_year=0.004)

    return [None, constant_i, linear_i]


def get_profit_data(bond, inflation_models, step=0.005, steps=8):
    
    coupon_rates = [t * step for t in range(1, steps)]
    balloon_payments = [t * 0.1 for t in range(steps)]
    coupon_heading, balloon_headings = zip(*list(product(coupon_rates, balloon_payments)))
    profit_data = [coupon_heading, balloon_headings]

    for im in inflation_models:
        bond.inflation_model = im
        profits = []
        for cr in coupon_rates:
            bond.coupon_rate = cr
            for br in balloon_payments:
                bond.baloon_payment = br * bond.price
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

    bond = PartiallyAmortizingBond(
        face_value=face_value,
        price=price,
        maturity=maturity,
        payment_frequency=payment_frequency,
        coupon_rate=0,  # 5% coupon rate
        baloon_payment=500,  # Example balloon payment at the end
        inflation_model=None
    )


    inflation_models = get_inflation_models()
    profit_data = get_profit_data(bond, inflation_models)
    headers = ['Coupon rate', 'Balloon payment', 'No inflation', 'Constant', 'Linear']

    print(profit_data)

    save_profit_data(profit_data, headers, 'part-amort.csv')

main()