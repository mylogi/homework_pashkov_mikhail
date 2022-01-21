# Example 1

# l_1 = [1, 2, 3]
# iter_l = iter(l_1)
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))


# Example 2

# class Reverse:
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         else:
#             self.index -= 1
#             return self.data[self.index]
#
#
# my_str = 'python'
# for elem in my_str:
#     print(elem, end='')
# print()
# for elem in Reverse(my_str):
#     print(elem, end='')
# print()


# Example 3

# def Reverse(data):
#     for i in range(len(data) - 1, - 1, - 1):
#         yield data[i]
#
#
# my_str = 'python'
# for elem in my_str:
#     print(elem, end='')
# print()
# for elem in Reverse(my_str):
#     print(elem, end='')
# print()


# Example 4

# class MySquareIterator:
#
#     def __init__(self, _from, _to, step=1):
#         self.idn = _from
#         self.to = _to
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idn > self.to:
#             raise StopIteration
#         val = self.idn ** 2
#         self.idn += self.step
#         return val
#
#
# c = MySquareIterator(1, 10, 2)
#
# for i in c:
#     print(i)


# Example 5

# def my_squares_generator(_from, _to, step=1):
#     for i in range(_from, _to + 1, step):
#         yield i ** 2
#
#
# c = my_squares_generator(1, 10, 2)
# for i in c:
#     print(i)


# Example 6

# squares = (it for it in range(10))
# squares_l = [it for it in range(10)]
#
# print(squares)
# print(squares_l)


# Example 7

# def echo(value=None):
#     print("Execution starts when 'next()' is called for the first time.")
#     try:
#         while True:
#             try:
#                 value = (yield value)
#             except Exception as e:
#                 value = e
#     finally:
#         print("Don't forget to clean up when 'close()' is closed.")
#
#
# gen = echo(1)
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# print(gen.send(2))
#
# gen.throw(TypeError, "spam")
#
# print(gen.send(10))
# print(gen.send(100))
# print(gen.close())


# Example 8

# import itertools, random
#
# # help(itertools.count)
# print(list(zip(itertools.count(start=1), ["A", "B", "C"], ['a', 'b', 'c'])))
#
# # help(itertools.chain)
# for it in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
#     print(it)
#
# a_list = ['abc', [1, 2, 3, [4, 5]], ('d', 'e', 'f')]
# for it in itertools.chain.from_iterable(a_list):
#     print(it)


# Example 9

# import itertools, random
#
# help(itertools.compress)
#
# c = list(itertools.compress([random.randint(1, 10) for i in range(10)],
#                             [random.randint(0, 1) for i in range(10)]))
# print(c)


# Example 10

# import itertools, random
#
# help(itertools.takewhile)
#
# a_list = [(1, 'B'), (2, 'C'), (3, 'A'), (4, 'D'), (4, 'D')]
# c = list(itertools.takewhile(lambda x: x[0] < 3, a_list))
# print(c)


# Example 11

# import itertools, random
# 
# help(itertools.starmap)
# 
# a_list = [[1, 2, 3], [4, 5, 6, 7, 8, 89, 7, 6, 4, 3, 1, 3, 2], [0]]
# 
# 
# def temp(*args):
#     return sum(args)
# 
# 
# print(list(itertools.starmap(temp, a_list)))
