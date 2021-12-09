"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """This is the division class"""
    def get_result(self):
        """Return the quotient of value_a and value_b"""
        difference = self.values[0]
        for value in self.values[1:len(self.values)]:
            try:
                difference =  difference / value
            except ZeroDivisionError:
                return ZeroDivisionError ('Division by Zero')
        return difference