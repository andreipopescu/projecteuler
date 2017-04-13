

def fibonacci(condition):
    """
    Generate fibonacci sequence
    :param condition: callback function called with index and value parameters 
    :return: fibonacci sequence 
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
