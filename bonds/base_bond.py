# bonds/base_bond.py

class Bond:
    """
    Base class for all bond types.
    """

    def __init__(self, face_value: float, maturity: float, interest_rate_model):
        """
        Initialize a bond with common attributes.

        :param face_value: The face value (principal) of the bond.
        :param maturity: The time to maturity (in years).
        :param interest_rate_model: The interest rate model to use for valuation.
        """
        self.face_value = face_value
        self.maturity = maturity
        self.interest_rate_model = interest_rate_model

    def calculate_price(self) -> float:
        """
        Calculate the present value (price) of the bond.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement calculate_price().")

    def calculate_yield(self) -> float:
        """
        Calculate the yield to maturity (YTM) of the bond.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement calculate_yield().")

    def adjust_for_inflation(self, inflation_rate: float) -> float:
        """
        Adjust the nominal value to its real value using the inflation rate.

        :param nominal_value: The nominal value to adjust (e.g., bond price or face value).
        :param inflation_rate: The annual inflation rate (e.g., 0.02 for 2%).
        :return: The real value of the bond.
        """
        return self.face_value / (1 + inflation_rate) ** self.maturity