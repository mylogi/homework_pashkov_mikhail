""" Task 1

Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""


# Program/Functions:

def oops():
    raise KeyError


# raise IndexError


def another_function():
    try:
        oops()
    except IndexError:
        print('Catch error!')


if __name__ == '__main__':
    another_function()
