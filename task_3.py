"""

One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the “partition
limit”). Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. Perform
analysis using different list sizes for the partition limit.

"""

# Solution:


# def quick_sort(array):
#     quick_sort_helper(array, 0, len(array) - 1)
#
#
# def quick_sort_helper(array, first, last):
#     if first < last:
#         split_point = partition(array, first, last)
#
#         quick_sort_helper(array, first, split_point - 1)
#         quick_sort_helper(array, split_point + 1, last)
#
#
# def partition(array, first, last):
#     pivot_value = array[first]
#
#     left_mark = first + 1
#     right_mark = last
#
#     done = False
#     while not done:
#
#         while left_mark <= right_mark and array[left_mark] <= pivot_value:
#             left_mark = left_mark + 1
#
#         while array[right_mark] >= pivot_value and right_mark >= left_mark:
#             right_mark = right_mark - 1
#
#         if right_mark < left_mark:
#             done = True
#         else:
#             temp = array[left_mark]
#             array[left_mark] = array[right_mark]
#             array[right_mark] = temp
#
#     temp = array[first]
#     array[first] = array[right_mark]
#     array[right_mark] = temp
#
#     return right_mark
#
#
# def selection_sort(array):
#     for fill_slot in range(len(array) - 1, 0, -1):
#         position_max = 0
#         for location in range(1, fill_slot + 1):
#             if array[location] > array[position_max]:
#                 position_max = location
#
#         temp = array[fill_slot]
#         array[fill_slot] = array[position_max]
#         array[position_max] = temp
#
#
# list_01 = [random.randint(1, 100) for _ in range(3)]
# selection_sort(list_01)
# print(list_01, '\n')
