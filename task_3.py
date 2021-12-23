"""The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The
program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""


# Program:

# def name_check():
#     name = 'mikhail'
#     user_name = input('Enter your name: ')
#
#     if name == user_name.lower():
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     print(name_check())

# Program_2:

# def name_check():
#     name = 'mikhail'
#     user_name = input('Enter your name: ')
#
#     return True if name == user_name.lower() else False
#
#
# if __name__ == '__main__':
#     print(name_check())

# Program_3:

# def name_check():
#     name = 'mikhail'
#     user_name = input('Enter your name: ')
#
#     return name == user_name.lower()
#
#
# if __name__ == '__main__':
#     print(name_check())

# Program_4:

# print(f'Name is {"" if "mikhail" == input("Enter the name: ").lower() else "not "}equal to name from input')

# Program_5:

def is_name_valid(name_from_storage: str, name_from_input: str) -> bool:
    return name_from_storage == name_from_input.lower()


def name_check() -> None:
    name = 'mikhail'
    user_name = input('Enter your name: ')

    is_equal = is_name_valid(name, user_name)

    message_about_state = '' if is_equal else ' not'
    print(f'Name {name.title()} is{message_about_state} equal to {user_name.title()}')


if __name__ == '__main__':
    name_check()
