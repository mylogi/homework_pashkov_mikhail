"""

A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list and the second pass
moves “down.” This alternating pattern continues until no more passes are necessary. Implement this variation and
describe under what circumstances it might be appropriate.

"""

# Solution:
import random


def bubble_sort_up(array):
    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


def bubble_sort_down(array):
    for pass_num in range(len(array) - 1):
        for i in range(len(array) - 1, pass_num, -1):
            if array[i] > array[i - 1]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp


list_01 = [random.randint(1, 100) for _ in range(26)]
bubble_sort_up(list_01)
print(list_01, '\n')
bubble_sort_down(list_01)
print(list_01, '\n')
