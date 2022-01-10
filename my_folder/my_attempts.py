# class Car():
#     total_number_of_car = 0
#
#     def __init__(self, brand, model, year, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.total_driven_km = 0
#         Car.total_number_of_car += 1
#
#     def repaint(self, color):
#         self.color = color
#
#     def drive(self, km_driven):
#         self.total_driven_km += km_driven
#
#
# car1 = Car('Volvo', 'V90', 2017, 'white')
# print(Car.total_number_of_car)
# car2 = Car('Ford', 'Focus', 2014, 'grey')
# print(Car.total_number_of_car)


# class FirstClass():
#     class_attr = 0
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def do_something(self, temp):
#         print(f'A: {self.a}. B: {self.b}')
#         return self.a + self.b, FirstClass(self.a + self.b, self.a + self.b)
#
#
# x = FirstClass(1, 2)
# y = FirstClass(3, 4)
#
# print(x.do_something(y))
# print(y.do_something(x))
# z = x.do_something(y)
# z = z[1]
# print(z.a)


# def test():
#     x = 1
#     print(x)
# print('x')
# test()


# spam = 1
#
#
# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
#
# scope_test()
# print("In global scape:", spam)
