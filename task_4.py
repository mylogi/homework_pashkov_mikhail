"""

def reverse(input_str: str) -> str:

    Function returns reversed input string
    reverse("hello") == "olleh"
    True
    reverse("o") == "o"
    True

"""


# Solution:

def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    if len(input_str) <= 0:
        return ''
    return input_str[-1] + reverse(input_str[:-1])


print(reverse('hello') == 'olleh')
print(reverse('o') == 'o')
print(reverse('make up me'))
