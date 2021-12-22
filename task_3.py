"""Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

Tips: Use random module to get random char from string)
"""
# Program:
import random

user_string = input('Enter your word: ')
user_string_length = len(user_string)


def random_string_func():
    if user_string.isalpha():
        print(user_string[0:random.randint(0, user_string_length)])


if __name__ == '__main__':
    random_string_func()
