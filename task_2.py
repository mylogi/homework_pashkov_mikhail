"""The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check that the
string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""


# Program:

def check_number(phone_number: str):
    if phone_number.isdigit() and len(phone_number) == 10:
        print(f'Mobile number: {phone_number}')
    else:
        print('Verification error')


if __name__ == '__main__':
    check_number('3809976411')
    check_number('809976411')
    check_number('b809976411')
