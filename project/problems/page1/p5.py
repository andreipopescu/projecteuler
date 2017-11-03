"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
import sys


def check(number):
    return all(number % x == 0 for x in range(1, 21))


def problem():
    return next(x for x in range(1, sys.maxsize) if check(x))



