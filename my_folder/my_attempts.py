# BIG-O
# Example 1:
#
# import time
# from random import randrange
#
# def find_min(alist):
#     overallim = alist[0]
#     for i in alist:
#         issmallest = True
#         for j in alist:
#             if i > j:
#                 issmallest = False
#         if issmallest:
#             overallim = i
#     return overallim
#
# def find_min(alist):
#     minsofar = alist[0]
#     for i in alist:
#         if i < minsofar:
#             minsofar = i
#     return minsofar
#
#
# print(find_min([5, 4, 3, 2, 1, 0]))
# print(find_min([0, 1, 2, 3, 4, 5]))
# print(find_min([7, 8, 10, 2, 3, 10, 11]))
#
# for listSize in range(1000, 10001, 1000):
#     alist = [randrange(100000) for x in range(listSize)]
#     start = time.time()
#     print(find_min(alist))
#     end = time.time()
#     print("size: %d time: %f" % (listSize, end - start))

#
#
# def fact(n):
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product
#
#
# print(fact(5))


# Example 2:
#
# def linear_algo(items):
#     for item in items:
#         print(item)
#
#     for item in items:
#         print(item)
#
#
# linear_algo([4, 5, 6, 8])
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = [2, 4, 6, 8, 10, 12]
#
# y = [4, 8, 12, 16, 20, 24]
#
# plt.plot(x, y, 'b')
# plt.xlabel('Inputs')
# plt.ylabel('Steps')
# plt.title('Linear Complexity')
# plt.show()
#
#
# def quadratic_algo(items):
#     for item in items:
#         for item2 in items:
#             print(item, ' ', item)
#
#
# quadratic_algo([4, 5, 6, 8])
