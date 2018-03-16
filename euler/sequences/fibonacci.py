
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
