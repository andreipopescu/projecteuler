"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_of_squares(number):
    """
    >>> sum_of_squares(7)
    140
    """
    return (number * (number + 1) * ((2 * number) + 1)) / 6


def gauss(number):
    """
    >>> gauss(100)
    5050
    """
    return number * (number + 1) / 2


def problem():
    number = 100
    return gauss(number)**2 - sum_of_squares(number)

