"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
the number of occurrences as values.

"""

# Program:
import re


def main():
    my_str = input('Enter your sentence: ')
    my_str_split_1 = re.split(r'[ ,:;\[\]]+', my_str)
    new_dictionary = {}
    print(my_str_split_1)
    for word in my_str_split_1:
        if word in new_dictionary:
            new_dictionary[word] += 1
        else:
            new_dictionary[word] = 1
    print(new_dictionary)


if __name__ == '__main__':
    main()
