"""

Implement the mergeSort function without using the slice operator.

"""
import random


def merge_sort(array):
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left_half = [array[i] for i in range(mid)]
    right_half = [array[i] for i in range(mid, len(array))]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1


if __name__ == '__main__':
    list_01 = [random.randint(1, 100) for _ in range(26)]
    merge_sort(list_01)
    print(list_01, '\n')
