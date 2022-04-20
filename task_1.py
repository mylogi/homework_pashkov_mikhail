""" Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a
valid email string.

Email validations:

https://help.xmatters.com/ondemand/trial/valid_email_format.htm

https://en.wikipedia.org/wiki/Email_address

"""


# Solution:

class EmailValidate:
    email_box = []
    valid_email_box = []
    check_dictionary = {
        'symbols': ['$', '#', '@', '/', '\\', '\'', '"', '+', '!', '?', '>', '<', ','],
        'domain': ['com', 'cc', 'org']
    }

    def __init__(self, email: str):
        self.email = email
        EmailValidate.email_box = [self.email]
        EmailValidate.valid_email_box = []
        EmailValidate.valid_email_box.append(EmailValidate.validate())
        EmailValidate.final_answer()

    @classmethod
    def validate(cls):
        data_list = EmailValidate.email_box
        for i in range(len(data_list)):
            for_check_list = data_list[i].split('@')
            if len(for_check_list) != 2:
                break
            if not for_check_list[0][-1].isalpha() and not for_check_list[0][-1].isdigit():
                break
            if len(for_check_list[-1].split('.')) != 2:
                break
            if for_check_list[-1].split('.')[-1] not in EmailValidate.check_dictionary['domain']:
                break
            for j in EmailValidate.check_dictionary['symbols']:
                if j in for_check_list[0] or j in for_check_list[-1]:
                    break
            else:
                return data_list[i]

    @classmethod
    def final_answer(cls):
        data_for_check = EmailValidate.valid_email_box
        if data_for_check[0] is None:
            print('Invalid email. Please try again')
        else:
            print(f'Your email: {EmailValidate.valid_email_box[0]} is correct')


def main():
    new_email = EmailValidate('abc_def@mail.com')
    print(new_email.email_box)
    new_email_1 = EmailValidate('abc_def-@mail.com')
    print(new_email_1.email_box)
    new_email_2 = EmailValidate('abc_def22@mail.com')
    print(new_email_2.email_box)


if __name__ == '__main__':
    main()
