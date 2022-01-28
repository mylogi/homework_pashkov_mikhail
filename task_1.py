"""School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
should only be available to the teacher.

"""

# Solution:

from datetime import datetime

classroom = {
    'A': {'cabinet': 210, 'classroom_teacher': 'Alfred', 'classmates': []},
    'B': {'cabinet': 205, 'classroom_teacher': 'Agreed', 'classmates': []},
    'C': {'cabinet': 235, 'classroom_teacher': 'Homer', 'classmates': []}
}


class Person:

    def __init__(self, name, lastname, gender, year_of_birth, address, tel_number):
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.year_of_birth = year_of_birth
        self.address = address
        self.tel_number = tel_number

    def greetings(self):
        print(f'\nGreetings! My name is {self.name} {self.lastname}')

    def age(self):
        current_datetime = datetime.now()
        current_datetime_year = current_datetime.year
        age = current_datetime_year - self.year_of_birth
        print(f'\nToday I am {age} years old')


class Student(Person):

    def __init__(self, name, lastname, gender, year_of_birth, address, tel_number, which_class, classroom_teacher, gpa):
        super().__init__(name, lastname, gender, year_of_birth, address, tel_number)
        self.which_class = which_class
        self.classroom_teacher = classroom_teacher
        self.gpa = gpa

    def academic_performance(self):
        if self.gpa <= 3:
            print('\nMy performance is very low.')
        elif 3 < self.gpa <= 6:
            print('\nMy performance is a low')
        elif 6 < self.gpa <= 9:
            print('\nMy performance is satisfactory.')
        elif 9 < self.gpa <= 12:
            print('\nMy performance is high.')
        else:
            print("\nThis is a mistake, there is no such score.")

    def classmate(self):
        if self.which_class == 'A':
            for k, v in classroom.items():
                if k == 'A':
                    for key, val in v.items():
                        if key == 'classmates':
                            val.append(self.name)
        elif self.which_class == 'B':
            for k, v in classroom.items():
                if k == 'B':
                    for key, val in v.items():
                        if key == 'classmates':
                            val.append(self.name)
        elif self.which_class == 'C':
            for k, v in classroom.items():
                if k == 'C':
                    for key, val in v.items():
                        if key == 'classmates':
                            val.append(self.name)
        else:
            print('This is mistake!')


class Teacher(Person):

    def __init__(self, name, lastname, gender, year_of_birth, address, tel_number, subject, cabinet,
                 class_in_submission):
        super().__init__(name, lastname, gender, year_of_birth, address, tel_number)
        self.subject = subject
        self.cabinet = cabinet
        self.class_in_submission = class_in_submission


student_1 = Student('Michael', 'Pashkov', 'man', 2004, 'Gaffery st. 4', '0997526973', 'B', 'Alfred', 9)
student_1.greetings()
student_1.age()
student_1.academic_performance()
student_1.classmate()
print('\n', classroom['B'])
