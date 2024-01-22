import math
def fact(a):
    if not isinstance(a, int):
        raise TypeError("Integer number only")
    if a < 1:
        raise ValueError("Your number must not be less than zero")
    res = 1
    while a > 1:
        res *= a
        a -=1
    return res

print(fact(49))
