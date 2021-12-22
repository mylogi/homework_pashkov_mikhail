""" The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
"""


# Program:

def calculate_u_bd():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")

    if user_age.isdigit() and user_name.isalpha():
        user_age_add = int(user_age)
        user_age_add += 1
        print(f'Hello {user_name.title()}, on your next birthday you’ll be {user_age_add} years')
    else:
        print('Try once more')


if __name__ == '__main__':
    calculate_u_bd()
