# Example 1

# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.first_name.title() + ' ' + self.last_name.title()
#
#     @property
#     def initials(self):
#         return self.first_name[0].upper() + self.last_name[0].upper()
#
#
# cj = Person('carl', 'johnson')
# print(cj.full_name)
# print(cj.initials)
# cj.first_name = 'Buster'
# print(cj.full_name)
# print(cj.initials)


# Example 2

# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.first_name.title() + ' ' + self.last_name.title()
#
#     @property
#     def initials(self):
#         return self.first_name[0].upper() + self.last_name[0].upper()
#
#     @full_name.setter
#     def full_name(self, name):
#         first, last = name.split(' ')
#         self.first_name = first.title()
#         self.last_name = last.title()
#
#     @full_name.deleter
#     def full_name(self):
#         self.first_name = None
#         self.last_name = None
#         print('Deleted')
#
#
# cj = Person('carl', 'johnson')
# print(cj.full_name)
# print(cj.initials)
# # cj.full_name = 'Buster Karlson'
# del cj.full_name
# print(cj.first_name, cj.last_name)
# # print(cj.initials)


# Example 3

# class Test:
#     def __init__(self, var):
#         self._var = var
#
#     @property
#     def get_var(self):
#         """return value of_var"""
#         return self._var
#
#     @get_var.setter
#     def set_var(self, value):
#         self._var = value
#
#     @get_var.deleter
#     def det_var(self):
#         del self._var
#
#
# t = Test(1)
# print(t.get_var)
#
# t.set_var = 10
# print(t.get_var)


# Example 4

# class Test:
#     def __init__(self, x):
#         self.x = x
#
#     @staticmethod
#     def t(a, b):
#         return a + b
#
#
# t = Test(1)
# print(t.t(10, 20))


# Example 5

# class Base:
#     _x = 1
#
#     @classmethod
#     def test(cls):
#         return f'hello from class: {cls.__name__}, value: {cls._x}'
#
#
# b = Base
# print(b.test())
#
#
# class Derived(Base):
#     _x = 100
#
#
# d = Derived()
# print(d.test())


# Example 6

# class MyAttr:
#
#     def __get__(self, instance, owner):
#         print('get invoked')
#         return 42
#
#     def __set__(self, instance, value):
#         print('set invoked')
#
#
# class Base:
#     ...
#
#
# Base.a = 1
# Base.d = MyAttr()
# print(Base.d)
#
# print(Base.__dict__)
#
# b = Base()
# b.d = 20
# print(b.d)
#
# print(b.__dict__)
#
# print(b.__class__.__mro__)
#
# Base.d = 1
# print(Base.__dict__)
#
# b2 = Base()
# b.d = 20
# print(b.d)


# Example 7

# class MyAttr:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print('get invoked')
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print('set invoked')
#         if value > 0:
#             instance.__dict__[self.name] = value
#             return
#         raise ValueError('value mast be > 0')
#
#
# class ValidContainer:
#     x = MyAttr('x')
#     y = MyAttr('y')
#
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#
# q = ValidContainer(1, 2)
#
# print(q.x)
#
# print(q.__dict__)


# Example 8

# class MyAttr:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __set__(self, instance, value):
#         print('set invoked')
#         if value > 0:
#             instance.__dict__[self.name] = value
#             return
#         raise ValueError('value mast be > 0')
#
#
# class ValidContainer:
#     x = MyAttr('x')
#     y = MyAttr('y')
#
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#
# q = ValidContainer(1, 2)
#
# print(q.x)
#
# print(q.__dict__)


# Example 9

# import time
#
#
# class LongJourney:
#
#     def __init__(self):
#         self.val = self.calc_val()
#
#     def calc_val(self):
#         time.sleep(1)
#         return 42
#
#
# x = LongJourney()
# y = LongJourney()
# z = LongJourney()
#
# print(x.val)


# Example 10

# import time
#
#
# class MyAttr:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print('invoked')
#         if instance is None:
#             return self
#         val = instance.calc_val()
#         setattr(instance, self.name, val)
#         return val
#
#
# class LongJourney:
#     val = MyAttr('val')
#
#     def calc_val(self):
#         time.sleep(1)
#         return 42
#
#
# x = LongJourney()
# y = LongJourney()
# z = LongJourney()
#
# print(x.val)
# print(x.val)


# Example 11

# class ShowDescr:
#
#     def test(self, a):
#         return self + a
#
#
# print(ShowDescr.__dict__)
#
# ShowDescr().test
#
# x = ShowDescr.test.__get__(2)
# print(x)
#
# print(x(2))
