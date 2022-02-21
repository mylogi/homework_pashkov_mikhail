"""

Write a Python program to detect the number of local variables declared in a function.

"""


# Solution:

def counter_local_variables():
    x = 1
    y = 0
    z = 'yes'
    print('Name of local variables: ', dir())
    print('Local variables: ', locals())
    # print(counter_local_variables.__code__)
    print('A number of local variables: ', counter_local_variables.__code__.co_nlocals)


def main():
    counter_local_variables()


if __name__ == '__main__':
    main()
