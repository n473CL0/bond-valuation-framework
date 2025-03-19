# bonds/zero_coupon_bond.py

from bonds.base_bond import Bond

class ZeroCouponBond(Bond):
    """
    A class representing a zero-coupon bond.
    """

    def calculate_cash_flows(self) -> list:
        """
        Calculate the cash flows of the zero-coupon bond.

        :return: A list of tuples (time_period, cash_flow).
        """
        return [(self.maturity, self.face_value)]