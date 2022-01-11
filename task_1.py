"""A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
attributes. Make another method called talk() which makes prints a greeting from the person containing, for example
like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

"""


class Person:
    firstname = 'Carl'
    lastname = 'Johnson'
    age = 26

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self, first_name=firstname, last_name=lastname, age_2=age):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age_2
        print(f'Hello, my name is {first_name} {last_name} and I’m {age_2} years old')


def main():
    carl = Person('John', 'Carlson', 62)
    print(carl.firstname, carl.lastname, carl.age)
    carl.talk('Carl', 'Johnson', 26)


if __name__ == '__main__':
    main()
