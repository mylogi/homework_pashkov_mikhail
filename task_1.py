"""

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

"add called with 4, 5"


def logger(func):

    pass



@logger

def add(x, y):

    return x + y



@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

"""


# Solution:

def logger(func):
    def wrapper(*args, **kwargs):
        # print(locals())
        # print(func.__name__)
        x = str(args)
        y = x[1:-1]
        print(f'"{func.__name__} called with {y}"')

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


def main():
    add(2, 3)
    square_all(2, 3, 4)


if __name__ == '__main__':
    main()
