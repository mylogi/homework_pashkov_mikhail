"""String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string
length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: ' x'

Expected Result: Empty String

Tips:
    Use built-in function len() on an input string
    Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""


# Program:

def string_redactor(input_string):
    if len(input_string) >= 2:
        print(input_string[0:2], input_string[-2:], sep='')
    else:
        print('Empty String')


if __name__ == '__main__':
    string_redactor('helloworld')
    string_redactor('my')
    string_redactor('x')
