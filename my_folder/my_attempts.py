# Example 1

# import time
#
#
# def time_function(f):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = f(*args, **kwargs)
#         end = time.time()
#         print(f.__name__ + " took " + str((end - start) * 1000) + "ms")
#         return result
#     return wrapper
#
#
# @time_function
# def square_numbers(num_list):
#     new_list = []
#     for num in num_list:
#         new_list.append(num ** 2)
#     return new_list
#
#
# @time_function
# def cube_numbers(num_list):
#     new_list = []
#     for num in num_list:
#         new_list.append(num ** 3)
#     return new_list
#
#
# my_list = [1, 2, 3, 4, 5, 6]
# my_list_squared = square_numbers(my_list)
# my_list_cubed = cube_numbers(my_list)
# print(my_list_squared)
# print(my_list_cubed)


# Example 2

# def first_decorator(func):
#     def wrap():
#         print('before')
#         func()
#         print('after')
#
#     return wrap
#
#
# @first_decorator
# def test():
#     """test function docs"""
#     print('inside text')
#
#
# test()
# print(test.__name__)
# print(test.__doc__)


# Example 3

# from functools import wraps
#
#
# def first_decorator(func):
#     @wraps(func)
#     def wrap():
#         print('before')
#         func()
#         print('after')
#
#     return wrap
#
#
# @first_decorator
# def test():
#     """test function docs"""
#     print('inside text')
#
#
# test()
# print(test.__name__)
# print(test.__doc__)


# Example 4

# from functools import wraps
#
#
# def add_brake_log(size=2):
#     def add_brake_log_dec(func):
#         @wraps(func)
#         def wrap(*args, **kwargs):
#             for _ in range(size):
#                 print("_" * 80)
#             func(*args, **kwargs)
#             for _ in range(size):
#                 print("_" * 80)
#
#         return wrap
#
#     return add_brake_log_dec
#
#
# @add_brake_log(size=2)
# def test():
#     """test function docs"""
#     print('inside text')
#
#
# test()
# print(test.__name__)
# print(test.__doc__)
