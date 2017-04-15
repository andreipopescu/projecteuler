"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    num_str = str(number)
    left, right = num_str[:3], num_str[-3:][::-1]
    return left == right


def problem():
    n = 999
    m = n
    while m:
        product = n * m
        if is_palindrome(product):
            return product
        else:
            if m >= n:
                m -= 1
            else:
                n -= 1
    return -1
