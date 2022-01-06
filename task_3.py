"""

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to
`i` squared

"""


# Solution:

def main():
    new_list = [(i, j) for i in range(1, 11) for j in range(i ** 2)]
    print(new_list)


if __name__ == '__main__':
    main()
