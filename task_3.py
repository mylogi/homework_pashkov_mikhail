"""A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep
things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second
parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

    the call make_operation(‘+’, 7, 7, 2) should return 16
    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
    the call make_operation(‘*’, 7, 6) should return 42
"""


# The Simple calculator:
def make_operation(*args):
    if str(args[0]) == '+':
        return_value = 0
        for item in args[1:]:
            return_value += item

    elif str(args[0]) == '-':
        return_value = args[1]
        for item in args[2:]:
            return_value -= item

    elif str(args[0]) == '*':
        return_value = 1
        for item in args[1:]:
            return_value *= item

    else:
        return_value = 'WRONG ARITHMETIC OPERATOR. TRY: "+", "-", "*"'

    print(return_value)


if __name__ == '__main__':
    make_operation('+', 7, 7, 2)
    make_operation('-', 5, 5, -10, -20)
    make_operation('*', 7, 6)
