# # y = (1, 2, 3)
# # print(y)
# #
# # y = y[:1] + (101,) + y[2:]
# # print(y)
#
# l = [1, 2, 3, 4, 5, 6, [7, 8], 7]
# x = l.pop(0)
#
# print(x)
# print(l)

# ssss = list(range(0, -11, -2))
#
# print(ssss)

# range_len = 10
# range_object = range(range_len)
# i = 0
# t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# while i < range_len:
#     print(range_object[i], t[i])
#     i += 1

# x = [1, 2, 3, 4]
# print(id(x), x)
#
# x.append(5)
# print(id(x), x)

# x = (1, 2, 3, 4)
# print(id(x), x)
#
# x = x + (5, )
# print(id(x), x)

# a = ['b', 'c', 'd']
# b = a
# print(a, b)
# print(a == b)
# print(id(a), id(b))

# a2 = ['a', 'b', 'c']
# b2 = ['a', 'b', 'c']
# print(a2 == b2)
# print(a2, b2)
# print(id(a2), id(b2))
# print(a2 is b2)
#
# b2[0] = 'A'
# print(a2, b2)


# x = [1, 10, -5.0, -2, 13]
# print('sorted', sorted(x))
# print('original', x)
#
# x.sort()
# print(x)


# a = ['a', 1, True]
# b = a[:]
# print(a, b, sep='\n')
# print(id(a), id(b))


# l = [1, 2, 3, ['Yola', 'Bola', 'Smola', [True, False]]]
# l[3][3][1] = 'Wrong'
# print(l)


# c = [True, False]
# b = ['Yola', 'Bola', 'Smola', c]
# a = [1, 2, 3, b]
#
# # c[0] = 'Wrong'
# # print(a)
#
# new_a = a.copy()
# c[0] = 'HELLO'
# print(new_a, a, sep='\n')
#
# import copy
#
# new_a1 = copy.deepcopy(a)
# print(new_a1)
#
# c[0] = 'West'
# print(new_a1)
# print(a)
#
# a[3][3][0] = 'TEST1'
# print(new_a1)
# print(a)


# a = (1, 2, 3, 4, 10, 4, 6, 8, 9)
# x = sorted(a)
# print(x)


# countries = ['Ukraine', 'Belarus', 'Romania', 'Serbia', 'USA', 'Germany', 'France', 'Poland']
# for i, country in enumerate(countries):
#     countries[i] = (country, i+1)
# print(countries)


# sevens = []
# for i in range(1, 71):
#     if i % 7 == 0:
#         sevens.append(i)
# print(sevens)


# sevens = []
# for i in range(0, 71, 7):
#     sevens.append(i)
# print(sevens)


# sevens = []
# i = 0
# while i <= 70:
#     sevens.append(i)
#     i += 7
# print(sevens)


# import random
#
# points = 0
# while True:
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     print('points: ' + str(points))
#     answer = input(str(x) + '+' + str(y) + '=? (type q to quit): ')
#     if answer == 'q':
#         break
#     elif int(answer) != x+y:
#         print('No points for you')
#         continue
#     print('Good job')
#     points += 1


# country = {'name': 'Sweden', 'capital': 'Stockholm',
#            'largest_cities': ['Stockholm', 'Gothenburg', 'Malmo']}
# # country['population'] = 10000000
# # print(country)
# # country.update({'population': 10000000, 'language': 'Swedish'})
# # print(country)
# # del country['largest_cities']
# # print(country)
# for key, value in country.items():
#     print(key, ':', value)
