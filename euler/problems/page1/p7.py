"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# from utils import primes
from euler.sequences import primes


def problem():
    prime = 0
    for x in primes(lambda x: x <= 10001):
        prime = x
    return prime



