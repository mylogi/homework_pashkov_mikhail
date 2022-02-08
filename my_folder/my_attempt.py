# Example 1:

# def fibonacci_search(lys, val):
#     fib_m_minus_2 = 0
#     fib_m_minus_1 = 1
#     fib_m = fib_m_minus_1 + fib_m_minus_2
#     while (fib_m < len(lys)):
#         fib_m_minus_2 = fib_m_minus_1
#         fib_m_minus_1 = fib_m
#         fib_m = fib_m_minus_1 + fib_m_minus_2
#     index = -1;
#     while (fib_m > 1):
#         i = min(index + fib_m_minus_2, (len(lys) - 1))
#         if (lys[i] < val):
#             fib_m = fib_m_minus_1
#             fib_m_minus_1 = fib_m_minus_2
#             fib_m_minus_2 = fib_m - fib_m_minus_1
#             index = i
#         elif (lys[i] > val):
#             fib_m = fib_m_minus_2
#             fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
#             fib_m_minus_2 = fib_m - fib_m_minus_1
#         else:
#             return i
#     if (fib_m_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
#         return index + 1;
#     return -1
#
#
# print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6))


# Example 2:

# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
#
#
# def ExponentialSearch(lys, val):
#     if lys[0] == val:
#         return 0
#     index = 1
#     while index < len(lys) and lys[index] <= val:
#         index = index * 2
#     return BinarySearch(lys[0:min(index, len(lys))], val)
#
#
# print(ExponentialSearch([1, 2, 3, 4, 5, 6, 7, 8], 3))


# Example 3:

# def InterpolationSearch(lys, val):
#     low = 0
#     high = (len(lys) - 1)
#     while low <= high and val >= lys[low] and val <= lys[high]:
#         index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
#         if lys[index] == val:
#             return index
#         if lys[index] < val:
#             low = index + 1;
#         else:
#             high = index - 1;
#     return -1
#
#
# print(InterpolationSearch([1, 2, 3, 4, 5, 6, 7, 8], 6))


# Example 4:

# class User:
#
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation
#
#     def __eq__(self, other):
#         return self.name == other.name \
#                and self.occupation == other.occupation
#
#     def __str__(self):
#         return f'{self.name} {self.occupation}'
#
#
# u1 = User('John Doe', 'gardener')
# u2 = User('John Doe', 'gardener')
#
# if (u1 == u2):
#     print('same user')
#     print(f'{u1} == {u2}')
# else:
#     print('different users')
#
# # users = {u1, u2}
# # print(len(users))


# Example 5:

# class User:
#
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation
#
#     def __eq__(self, other):
#         return self.name == other.name \
#                and self.occupation == other.occupation
#
#     def __hash__(self):
#         return hash((self.name, self.occupation))
#
#     def __str__(self):
#         return f'{self.name} {self.occupation}'
#
#
# u1 = User('John Doe', 'gardener')
# u2 = User('John Doe', 'gardener')
#
# users = {u1, u2}
#
# print(len(users))
#
# if (u1 == u2):
#     print('same user')
#     print(f'{u1} == {u2}')
# else:
#     print('different users')
#
# print('------------------------------------')
#
# u1.occupation = 'programmer'
#
# users = {u1, u2}
#
# print(len(users))
#
# if (u1 == u2):
#     print('same user')
#     print(f'{u1} == {u2}')
# else:
#     print('different users')
