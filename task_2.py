"""Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers

"""

# Function:
import random


def first_list():
    list_number_one = []
    i_1 = 0
    while i_1 < 10:
        list_number_one.append(random.randint(0, 99))
        i_1 += 1
    print(list_number_one)
    return list_number_one


def second_list():
    list_number_two = []
    i_2 = 0
    while i_2 < 10:
        list_number_two.append(random.randint(0, 99))
        i_2 += 1
    print(list_number_two)
    return list_number_two


def compare_lists():
    list_number_01 = first_list()
    list_number_02 = second_list()
    list_sum = list_number_01 + list_number_02
    result_list = [x for x in list_sum if x in list_number_01 and x in list_number_02]
    return list(set(result_list))


def main():
    result_list = compare_lists()
    if not result_list:
        print('There is no data.')
    else:
        print(f'List after comparison without duplicates: {result_list}')


if __name__ == '__main__':
    main()
