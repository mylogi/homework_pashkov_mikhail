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


# Dictionary:
def build_pet(species, name, **pet_info):
    pet = {}
    pet['species'] = species
    pet['name'] = name
    for key, value in pet_info.items():
        pet[key] = value
    return pet


my_pet = build_pet('Husky', 'Doge', color='White', age=2)
print(my_pet)

"""A tree of size
   *
  ***
 *****
"""


def print_tree(n):
    for i in range(n):
        for j in range(n - i):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print()


print_tree(7)
