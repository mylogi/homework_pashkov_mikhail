"""Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.

"""


# Sample:

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        print(self.age * Dog.age_factor)


def main():
    dog_1 = Dog(7)
    dog_1.human_age()


if __name__ == '__main__':
    main()
