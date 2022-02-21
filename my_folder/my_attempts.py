# Example 1

# def add_five(x):
#     return x + 5
#
#
# def do_twice(f):
#     def resulting_func(x):
#         return f(f(x))
#
#     return resulting_func
#
#
# result = do_twice(add_five)
# print(result(5))


# import math
#
#
# def make_cylinder_volume_function(r):
#     def volume(h):
#         return math.pi * r ** 2 * h
#
#     return volume
#
#
# volume_or_r10 = make_cylinder_volume_function(10)
# print(volume_or_r10(30)/(30*100))


# Example 3

# def test(word):
#     return f"Test {word}"
#
# test
#
# x = test
#
# print(x)
#
# x.__name__
#
# print(x('this'))
#
# # del x
# #
# # x


# Example 4

# word = 'Test'
# command = 'up'
#
#
# def up(word):
#     print(word.upper())
#
#
# def down(word):
#     print(word.lower())
#
#
# def default():
#     print('Unknown command')
#
#
# command_dict = {
#     "up": up,
#     "down": down
# }
#
# if command in command_dict:
#     command_dict[command](word)
# else:
#     default()
#
# func = command_dict.get(command, default)
# func('HELLO')


# Example 5

# word = 'Test'
# command = 'down'
#
#
# def up(word):
#     print(word.upper())
#
#
# def down(word):
#     print(word.lower())
#
#
# def default():
#     print('Unknown command')
#
#
# def process(command):
#     command_dict = {
#         "up": up,
#         "down": down
#     }
#
#     if command in command_dict:
#         return command_dict[command]
#     else:
#         return default
#
#
# process('up')('Test1')


# Example 6

# def test(word):
#     def low(it):
#         if it.isdigit():
#             return 'N'
#         return it.lower()
#
#     res = ' '
#     for i in word:
#         res += low(i)
#     return res
#
#
# print(test('Hello1'))


# Example 7

# def logger_func(func, var):
#     print('before execution')
#     func(var)
#     print('after execution')
#
#
# def test(name):
#     print(f'My name is {name}')
#
#
# logger_func(test, 'SpiderMan')


# Example 8

# def logger_func(func, *args, **kwargs):
#     print('before execution')
#     func(*args, **kwargs)
#     print('after execution')
#
#
# def test(*args, **kwargs):
#     print('Args: ', args, type(args))
#     print('Kwargs: ', kwargs, type(kwargs))
#
#
# logger_func(test, 'SpiderMan', "Batman", x=1)


# Example 9

# class Adder:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, x):
#         return self.n + x
#
#
# x = Adder(10)
#
# print(x(10))


# Example 10

# x = [1, 2, 3, 4, 5]
#
#
# def sqr(item):
#     return item ** 2
#
#
# res = [sqr(it) for it in x]
# print(res)
#
# print(list(map(sqr, x)))

# Example 11

# x = [1, 2, 3, 4, 5]
#
#
# def sqr(item):
#     return item ** 2
#
#
# res = [sqr(it) for it in x]
# print(res)
#
# print(list(map(sqr, x)))
#
#
# def my_pow(item, power):
#     return item ** power
#
# powers = [2, 3, 4, 5]
#
# print([my_pow(x[i], powers[i]) for i in range(len(powers))])


# Example 12

# from timeit import timeit
#
# x = [1, 2, 3, 4, 5]
#
#
# def my_pow(item, power):
#     return item ** power
#
#
# powers = [2, 3, 4, 5]
#
# # print([my_pow(x[i], powers[i]) for i in range(len(powers))])
#
# print(timeit('[my_pow(x[i], powers[i]) for i in range(len(powers))]',
#              number=1000,
#              globals={'x': x, 'powers': powers, 'my_pow': my_pow}))
#
# print(timeit('list(map(my_pow, x, powers))',
#              number=1000,
#              globals={'x': x, 'powers': powers, 'my_pow': my_pow}))


# Example 12

# import sys
#
# x = [1, 2, 3, 4, 5]
#
#
# def my_pow(item, power):
#     return item ** power
#
#
# powers = [2, 3, 4, 5]
#
# # print([my_pow(x[i], powers[i]) for i in range(len(powers))])
#
# print(sys.getsizeof(map(my_pow, x, powers)))
#
# print(sys.getsizeof(list(map(my_pow, x, powers))))


# Example 13

# x = [1, 2, 3, 5, 36, 7, 8, 0]
#
# print(list(filter(lambda it: it > 2, x)))
# print(list(filter(None, x)))


# Example 14

# from functools import reduce
#
# help(reduce)
