"""Factorial Module"""


class Factorial:
    """Class for solving Factorial"""

    def solve(self, number):
        """Method for recursion"""
        # This is the base case
        # If number is 1, return 1.
        if number == 1:
            return number

        # Not the base case, get the answer to the smaller version of the same problem.
        result = self.solve(number - 1)
        # Return the result of the smaller version multiplied with the number
        return number * result
