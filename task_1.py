"""

from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:

    Returns  x ^ exp

        to_power(2, 3) == 8
    True

        to_power(3.5, 2) == 12.25
    True

        to_power(2, -1)
    ValueError: This function works only with exp > 0.

    pass

"""

# Solution:

from typing import Optional


def to_power(x: Optional[int | float], exp: int) -> Optional[int | float]:
    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    if x == 0 or exp == 0:
        return 1
    return to_power(x, exp - 1) * x


print(to_power(3, 3) == 27)
print(to_power(3.5, 2) == 12.25)
# print(to_power(2, -1))
