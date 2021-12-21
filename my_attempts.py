# Boolean data:

# if elif else:

# our_condition = 'no'
#
# if our_condition == 'yes':
#     print('I need to print "yes", because if statement evaluated True')
# else:
#     print('If statement evaluated False')
#
# if our_condition == 'yes':
#     print(f'I need to print "{our_condition}", because if statement evaluated True')
# elif our_condition == 'no':
#     print(f'I need to print "{our_condition}", because if statement evaluated False')
# else:
#     print('If statement evaluated false')
#
# x = 5
# if x < 2:
#     print('x < 2')
# elif x >= 5:
#     if x == 5:
#         print('got five')
#     else:
#         print('x > 5')
# elif x % 3 == 0:
#     print('x % 3 = 0')
# elif x < 7:
#     print('x < 7')
# else:
#     print('All other cases')

# While:

# our_threshold = 5
# i = 0
#
# while i < our_threshold:
#     print('Do important logic here.')
#     i += 1

# our_threshold = 10
# i = 0
#
# while i < our_threshold:
#     print(f'Variable i: {i}.', end=" ")
#     print('Do important logic here.')
#     i += 1
#     if i % 7 == 0:
#         print('Good reason to stop')
#         # break

# our_threshold = 23
# i = 0
#
# while i < our_threshold:
#     print(f'Variable i: {i}.', end=" ")
#     if i % 7 == 0:
#         print('Do very very important task and that`s it')
#         i += 1
#         continue
#
#     print('Do important logic here.')
#     i += 1

our_threshold = 6
i = 0

while i < our_threshold:
    print(f'Variable i: {i}.', end=" ")
    print('Do important logic here.')
    i += 1
    if i % 7 == 0:
        print('Something went wrong')
        everything_ok = False
        break
else:
    print('This very important logic will take place only if nothing broken')
