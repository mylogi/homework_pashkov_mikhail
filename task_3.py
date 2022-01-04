""" Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but
not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration

"""


# Created program:

def create_list():
    list_01 = []
    i_01 = 1
    while i_01 <= 100:
        list_01.append(i_01)
        i_01 += 1
    return list_01


def divisible():
    list_02 = create_list()
    list_03 = []
    i_02 = 0
    while i_02 < 100:
        a = list_02[i_02]
        x = a % 7
        y = a % 5
        if x == 0 and y != 0:
            list_03.append(a)
            i_02 += 1
        else:
            i_02 += 1
    return list_03


def main():
    print(create_list())
    print(divisible())


if __name__ == '__main__':
    main()
