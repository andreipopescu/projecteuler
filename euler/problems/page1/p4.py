"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    num_str_reversed = str(number)[::-1]
    return number == int(num_str_reversed)


def is_palindrome2(number):
    reverse = []
    while number > 0:
        reverse.append(number % 10)
        number //= 10
    return reverse == reverse[::-1]


def problem():
    return max(x * y
               for x in range(100, 1000)
               for y in range(100, 1000)
               if is_palindrome2(x * y))
