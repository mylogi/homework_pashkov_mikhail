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
