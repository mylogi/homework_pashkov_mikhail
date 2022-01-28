""" Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```

class Mathematician:

    pass



m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

"""


# Solution:

class Mathematician:

    def square_nums(list_1: list):
        print([i * i for i in list_1])

    def remove_positives(list_1: list):
        print([i for i in list_1 if i < 0])

    def filter_leaps(list_1: list):
        print([i for i in list_1 if i % 4 == 0])


m = Mathematician
m.square_nums([7, 11, 5, 4])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])
