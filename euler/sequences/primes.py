
def primes(stop_func):
    """ Generate primes
    >>> no_of_primes = 10
    >>> list(primes(lambda x: x <= no_of_primes))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    prime, count = 2, 1
    while stop_func(count):
        for d in range(2, prime):
            if prime % d == 0:
                break
        else:
            yield prime
            count += 1
        prime += 1
