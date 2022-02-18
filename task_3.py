"""

One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the “partition
limit”). Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. Perform
analysis using different list sizes for the partition limit.

"""


# Solution:


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


def quick_sort(array):
    if len(array) < 10:
        insertion_sort(array)

    else:
        quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)


def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp
    return right_mark


random_list_of_nums = [2, 33, 9, 36, 93, 3, 11, 14]
random_list_of_nums_2 = [33, 11, 92, 93, 1, 13, 4, 8, 9, 10]
quick_sort(random_list_of_nums)
quick_sort(random_list_of_nums_2)
print(random_list_of_nums)
print(random_list_of_nums_2)
