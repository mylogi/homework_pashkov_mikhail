# Examples of my attempts

# First:
def increment_value(l):
    for i in range(len(l)):
        l[i] += 1
    print("List inside of function: " + str(l))


original = [1, 2, 3]
increment_value(original)
print("List outside of function: " + str(original))


# Second:
def increment_value(l):
    l = [2, 3, 4]
    print("List inside of function: " + str(l))


original = [1, 2, 3]
increment_value(original)
print("List outside of function: " + str(original))

# Third:
lenth = len('Ukraine')

print(lenth)


# Fourth:
def sum_of_squares(x, y):
    return_value = x ** 2 + y ** 2
    return return_value


print(sum_of_squares(2, 3))


# Fifth:
def sum_of_squares(*args):
    return_value = 0
    for num in args:
        return_value += num ** 2
    return return_value


print(sum_of_squares(2, 3, 3, 5, 1, 6))
