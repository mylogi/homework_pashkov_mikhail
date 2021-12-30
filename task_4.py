"""The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then
responds with a message accordingly.

"""

# Program:
import random

x = random.randint(0, 1000)
y = random.randint(0, 1000)


def def_of_dictionary(first_variable: int, second_variable: int) -> dict:
    dictionary_of_expression = {
        f'{x} + {y} =': x + y,
        f'{x} * {y} =': x * y,
        f'{x} / {y} =': x / y
    }
    return dictionary_of_expression


def print_of_key():
    print_dictionary = def_of_dictionary(x, y)
    i = 1
    for keys in print_dictionary.keys():
        print(keys)


print_of_key()
