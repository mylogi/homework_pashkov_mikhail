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
# class Truck(Car):
#
#     def __init__(self, brand, model, year, color, trailers):
#         super().__init__(brand, model, year, color)
#         self.trailers = trailers
#
#     def attach_trailer(self, num_of_trailers=1):
#         self.trailers += num_of_trailers
#
#     def detach_trailers(self, num_of_trailers=1):
#         self.trailers -= num_of_trailers
#
#
# my_truck = Truck('MAN', 'TGX', 2012, 'black', 1)
# my_truck.repaint('green')
# print(my_truck.color)
# my_truck.attach_trailer()
# print(my_truck.trailers)
# my_truck.detach_trailers()
# print(my_truck.trailers)


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
#     def __repr__(self):
#         return (self.brand + ', ' + self.model + ' ' + str(self.year) + ' ' +
#                 self.color)
#
#     def __str__(self):
#         return self.brand + ' ' + self.model + ' ' + str(self.year)
#
#
# class Truck(Car):
#
#     def __init__(self, brand, model, year, color, trailers):
#         super().__init__(brand, model, year, color)
#         self.trailers = trailers
#
#     def attach_trailer(self, num_of_trailers=1):
#         self.trailers += num_of_trailers
#
#     def detach_trailers(self, num_of_trailers=1):
#         self.trailers -= num_of_trailers
#
#
# my_truck = Truck('MAN', 'TGX', 2012, 'black', 1)
# print(repr(my_truck))
# print(str(my_truck))


# class Base:
#     def __init__(self, x):
#         self.x = x
#
#
# class Test(Base):
#     pass
#
#
# x = Test(101)
# print(x.x)
# print(type(x))
#
#
# class Test2(Test):
#     pass
#
#
# x2 = Test2(102)
# print(x2.x)
#
# print(type(x2))


# class Base:
#     def test(self, word):
#         print(f'this is {word}')
#
#
# class Test(Base):
#     def test(self, word):
#         print(f'this is {word.upper()}')
#
#
# t1 = Base()
# t2 = Test()
#
# t1.test('hello')
# t2.test('hello')


# class Base:
#     def temp(self):
#         return 'temp'
#
#
# class SuperBase:
#     def temp(self):
#         return 'TEMP'
#
#
# class Base1:
#     def test1(self):
#         return 'test1'
#
#
# class Base2(Base):
#     def test(self):
#         return 'test'
#
#
# class Base3(SuperBase):
#     def test1(self):
#         return 'TEST1'
#
#
# # class Test(Base3, Base2, Base1):    # (Base3, Base2, Base1) -> x.test1
# #     pass
# #
# #
# # x = Test()
# #
# # print(x.test1())
#
#
# class Test3(Base3, Base2, Base1):  # (Base3, Base2, Base1) -> x.test1
#     pass
#
#
# z = Test3()
#
# print(z.temp())
