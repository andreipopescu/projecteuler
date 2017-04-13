from src.utils import fibonacci


def problem():
    result = 0
    for x in fibonacci(lambda i, v: v < 4000000):
        if x % 2 == 0:
            result += x
    return result
