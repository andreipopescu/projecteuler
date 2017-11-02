"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_next_prime(value):
    for x in range(2, int(value)):
        if value % x == 0:
            return x
    return value


def problem():
    result, target = 0, 600851475143
    while target > 1:
        prime = get_next_prime(target)
        result = prime if prime > result else result
        target /= prime
    return int(result)
