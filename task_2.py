"""

Write a Python program to access a function inside a function (Tips: use function, which returns another function)

"""


# Solution:

def need_access(a, b):
    print(a + b)


def access_function(a, b):
    return need_access(a, b)


def main():
    access_function(2, 3)
    access_function(1, 1)
    access_function(5, 7)


if __name__ == '__main__':
    main()
