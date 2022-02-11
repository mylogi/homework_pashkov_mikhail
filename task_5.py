"""
def sum_of_digits(digit_string: str) -> int:

    sum_of_digits('26') == 8
    True

    sum_of_digits('test')
    ValueError("input string must be digit string")

"""


# Solution:

def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if not digit_string:
        return 0
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[-1]) + sum_of_digits(digit_string[:-1])


print(sum_of_digits('26') == 8)
# print(sum_of_digits('test'))
