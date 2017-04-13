"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def problem():
    target = 13195
    for x in reversed(range(target)):
        if target % x == 0:
            return x
