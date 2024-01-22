def add(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise TypeError("Integers only")
    return x + y


def subtract(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise TypeError("Integers only")
    return x - y


def multiply(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise TypeError("Integers only")
    return x * y


def divide(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise TypeError("Integers only")
    if y != 0:
        return x / y
    raise ZeroDivisionError("Cannot divde by Zero")