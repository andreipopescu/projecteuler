def fibonacci(condition):
    """
    Generate fibonacci sequence
    Usage: 
        list(fibonacci(lambda i, v: i < 10))
        i -> 0 base index of current fibonacci number
        v -> value of current fibonacci index
    Examples:
        fibonacci(lambda i, v: i < 10) return first 10 fibonacci number
        fibonacci(lambda i, v: v < 10) return fibonacci number lower than 10
    :param condition: callback function called with index and value parameters 
    :return: fibonacci sequence as generator
    """
    index = 0
    _first, _second = 0, 1
    value = _first + _second
    while condition(index, value):
        yield value
        _first = _second
        _second = value
        value = _first + _second
        index += 1


def primes(stop_func):
    """
    >>> no_of_primes = 10
    >>> list(primes(lambda x: x <= no_of_primes))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    prime, count = 1, 1
    while stop_func(count):
        if prime in {1, 2}:
            prime += 1
            yield prime
            count += 1
        else:
            prime += 2
            for d in range(2, prime):
                if prime % d == 0:
                    break
            else:
                yield prime
                count += 1

