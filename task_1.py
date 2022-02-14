"""

A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list and the second pass
moves “down.” This alternating pattern continues until no more passes are necessary. Implement this variation and
describe under what circumstances it might be appropriate.

"""


# Solution:
# import random
#
#
# def bubble_sort_up(array):
#     for pass_num in range(len(array) - 1, 0, -1):
#         for i in range(pass_num):
#             if array[i] > array[i + 1]:
#                 temp = array[i]
#                 array[i] = array[i + 1]
#                 array[i + 1] = temp
#
#
# def bubble_sort_down(array):
#     for pass_num in range(len(array) - 1):
#         for i in range(len(array) - 1, pass_num, -1):
#             if array[i] > array[i - 1]:
#                 temp = array[i]
#                 array[i] = array[i - 1]
#                 array[i - 1] = temp
#
#
# list_01 = [random.randint(1, 100) for _ in range(26)]
# bubble_sort_up(list_01)
# print(list_01, '\n')
# bubble_sort_down(list_01)
# print(list_01, '\n')


def bubble_sort_2_ways(list_to_sort: list[int]) -> list[int]:
    swapped = True
    start_index = 0
    end_index = len(list_to_sort) - 1

    while swapped:
        swapped = False

        for i in range(start_index, end_index):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end_index -= 1

        for i in range(end_index - 1, start_index - 1, -1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True

        start_index += 1

    return list_to_sort


input_list = [5, 7, 6, 8, 4, 5, 0, 4, 7, 9, 2, 1]
bubble_sort_2_ways(input_list)
print(input_list)
