# Example 1 (Bubble sort):

# def bubble_sort(x: list):
#     # Swap the elements to arrange in order
#     for iter_num in range(len(x) - 1, 0, -1):
#         for idx in range(iter_num):
#             if x[idx] > x[idx + 1]:
#                 temp = x[idx]
#                 x[idx] = x[idx + 1]
#                 x[idx + 1] = temp
#
#
# list_1 = [19, 2, 31, 45, 6, 11, 121, 27]
# bubble_sort(list_1)
# print(list_1)

# def bubble_sort(nums):
#     # We set swapped to True so the loop looks runs at least once
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 # Swap the elements
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 # Set the flag to True so we'll loop again
#                 swapped = True
#
#
# # Verify it works
# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)


# Example 2 (Merge sort):

# def merge_sort(unsorted_list):
#     if len(unsorted_list) <= 1:
#         return unsorted_list
#     # Find the middle point and devide it
#     middle = len(unsorted_list) // 2
#     left_list = unsorted_list[:middle]
#     right_list = unsorted_list[middle:]
#
#     left_list = merge_sort(left_list)
#     right_list = merge_sort(right_list)
#     return list(merge(left_list, right_list))
#
#
# # Merge the sorted halves
# def merge(left_half, right_half):
#     res = []
#     while len(left_half) != 0 and len(right_half) != 0:
#         if left_half[0] < right_half[0]:
#             res.append(left_half[0])
#             left_half.remove(left_half[0])
#         else:
#             res.append(right_half[0])
#             right_half.remove(right_half[0])
#     if len(left_half) == 0:
#         res = res + right_half
#     else:
#         res = res + left_half
#     return res
#
#
# unsorted_list_by_user = [64, 34, 25, 12, 22, 11, 90]
# print(merge_sort(unsorted_list_by_user))

# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#
#     # We use the list lengths often, so its handy to make variables
#     left_list_length, right_list_length = len(left_list), len(right_list)
#
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             # We check which value from the start of each list is smaller
#             # If the item at the beginning of the left list is smaller, add it
#             # to the sorted list
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             # If the item at the beginning of the right list is smaller, add it
#             # to the sorted list
#             else:
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#
#         # If we've reached the end of the of the left list, add the elements
#         # from the right list
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         # If we've reached the end of the of the right list, add the elements
#         # from the left list
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#
#     return sorted_list
#
#
# def merge_sort(nums):
#     # If the list is a single element, return it
#     if len(nums) <= 1:
#         return nums
#
#     # Use floor division to get midpoint, indices must be integers
#     mid = len(nums) // 2
#
#     # Sort and merge each half
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#
#     # Merge the sorted lists into a new one
#     return merge(left_list, right_list)
#
#
# # Verify it works
# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_nums = merge_sort(random_list_of_nums)
# print(random_list_of_nums)


# Example 3 (Insertion sort):

# def insertion_sort(input_list):
#     for i in range(1, len(input_list)):
#         j = i - 1
#         nxt_element = input_list[i]
#         # Compare the current element with next one
#         while (input_list[j] > nxt_element) and (j >= 0):
#             input_list[j + 1] = input_list[j]
#             j = j - 1
#             input_list[j + 1] = nxt_element
#
#
# list_01 = [19, 2, 31, 45, 30, 11, 121, 27]
# insertion_sort(list_01)
# print(list_01)

# def insertion_sort(nums):
#     # Start on the second element as we assume the first element is sorted
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         # And keep a reference of the index of the previous element
#         j = i - 1
#         # Move all items of the sorted segment forward if they are larger than
#         # the item to insert
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         # Insert the item
#         nums[j + 1] = item_to_insert
#
#
# # Verify it works
# random_list_of_nums = [9, 1, 15, 28, 6]
# insertion_sort(random_list_of_nums)
# print(random_list_of_nums)


# Example 4 (Shell sort):

# def shellSort(input_list):
#     gap = len(input_list) // 2
#     while gap > 0:
#         for i in range(gap, len(input_list)):
#             temp = input_list[i]
#             j = i
#             # Sort the sub list for this gap
#             while j >= gap and input_list[j - gap] > temp:
#                 input_list[j] = input_list[j - gap]
#                 j = j - gap
#                 input_list[j] = temp
#         # Reduce the gap for the next element
#         gap = gap // 2
#
#
# list_01 = [19, 2, 31, 45, 30, 11, 121, 27]
# shellSort(list_01)
# print(list_01)


# Example 5 (Selection sort):

# def selection_sort(input_list):
#     for idx in range(len(input_list)):
#         min_idx = idx
#         for j in range(idx + 1, len(input_list)):
#             if input_list[min_idx] > input_list[j]:
#                 min_idx = j
#         # Swap the minimum value with the compared value
#         input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
#
#
# list_02 = [19, 2, 31, 45, 30, 11, 121, 27]
# selection_sort(list_02)
# print(list_02)

# def selection_sort(nums):
#     # This value of i corresponds to how many values were sorted
#     for i in range(len(nums)):
#         # We assume that the first item of the unsorted segment is the smallest
#         lowest_value_index = i
#         # This loop iterates over the unsorted items
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         # Swap values of the lowest unsorted element with the first unsorted
#         # element
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
#
# # Verify it works
# random_list_of_nums = [12, 8, 3, 20, 11]
# selection_sort(random_list_of_nums)
# print(random_list_of_nums)


# Example 6 (Heap sort):

# def heapify(nums, heap_size, root_index):
#     # Assume the index of the largest element is the root index
#     largest = root_index
#     left_child = (2 * root_index) + 1
#     right_child = (2 * root_index) + 2
#
#     # If the left child of the root is a valid index, and the element is greater
#     # than the current largest element, then update the largest element
#     if left_child < heap_size and nums[left_child] > nums[largest]:
#         largest = left_child
#
#     # Do the same for the right child of the root
#     if right_child < heap_size and nums[right_child] > nums[largest]:
#         largest = right_child
#
#     # If the largest element is no longer the root element, swap them
#     if largest != root_index:
#         nums[root_index], nums[largest] = nums[largest], nums[root_index]
#         # Heapify the new root element to ensure it's the largest
#         heapify(nums, heap_size, largest)
#
#
# def heap_sort(nums):
#     n = len(nums)
#
#     # Create a Max Heap from the list
#     # The 2nd argument of range means we stop at the element before -1 i.e.
#     # the first element of the list.
#     # The 3rd argument of range means we iterate backwards, reducing the count
#     # of i by 1
#     for i in range(n, -1, -1):
#         heapify(nums, n, i)
#
#     # Move the root of the max heap to the end of
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)
#
#
# # Verify it works
# random_list_of_nums = [35, 12, 43, 8, 51]
# heap_sort(random_list_of_nums)
# print(random_list_of_nums)


# Example 7 (Quick Sort):

# # There are different ways to do a Quick Sort partition, this implements the
# # Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
# def partition(nums, low, high):
#     # We select the middle element to be the pivot. Some implementations select
#     # the first element or the last element. Sometimes the median value becomes
#     # the pivot, or a random one. There are many more strategies that can be
#     # chosen or created.
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # If an element at i (on the left of the pivot) is larger than the
#         # element at j (on right right of the pivot), then swap them
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quick_sort(nums):
#     # Create a helper function that will be called recursively
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
#
#
# # Verify it works
# random_list_of_nums = [22, 5, 1, 18, 99]
# quick_sort(random_list_of_nums)
# print(random_list_of_nums)
