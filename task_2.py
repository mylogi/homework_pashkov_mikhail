""" Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
input function were not numbers, and if value b was zero (cannot divide by zero).

"""


# Functions:
def input_first_number():
    return input('Enter first number:')


def input_second_number():
    return input('Enter second number:')


def perform_calculation():
    a = input_first_number()
    b = input_second_number()
    return int(a) ** 2 / int(b)


def perform_exception():
    try:
        print(perform_calculation())
    except ZeroDivisionError:
        print('Wrong! Can`t be divided by zero!')
    except ValueError:
        print('Wrong! Can`t be divided non-numbers!')
    else:
        print('Its right!')


def main():
    perform_exception()


if __name__ == '__main__':
    main()
