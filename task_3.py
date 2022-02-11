"""
from typing import Optional
def mult(a: int, n: int) -> int:

    This function works only with positive integers

    mult(2, 4) == 8
    True

    mult(2, 0) == 0
    True

    mult(2, -4)
    ValueError("This function works only with positive integers")


"""


# Solution:


def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if a == 0:
        return 0
    return n + mult(a - 1, n)


print(mult(2, 6))
print(mult(2, 19))
print(mult(2, 26))
# print(mult(-1, 2))
# print(mult(2, -2))
