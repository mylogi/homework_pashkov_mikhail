"""The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers

"""

# Program:
import random


def append_my_list() -> int:
    my_list = []
    i = 10
    while i != 0:
        my_list.append(random.randint(0, 100))
        i -= 1
    print('Our list of values:', *my_list)
    my_list.sort()
    return my_list[9]


def main():
    print('Our the largest numer:', append_my_list())


if __name__ == '__main__':
    main()
