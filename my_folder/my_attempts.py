# Example_1

# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     # Abstract method
#     def talk(self):
#         raise NotImplementedError("Must be implemented by sub class")
#
#
# class Cat(Animal):
#     def talk(self):
#         print("Meow!")
#
#
# class Dog(Animal):
#     def talk(self):
#         print("Woof!")
#
#
# animals = [Cat('Garfield'), Dog('Hans'), Cat('Maja')]
#
# for animal in animals:
#     animal.talk()


# Example_2

# import turtle as t
#
#
# class Shape:
#
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def draw_shape(self):
#         raise NotImplementedError("Sub class must implement abstract method")
#
#
# class Circle(Shape):
#
#     def draw_shape(self):
#         t.setx(self.x)
#         t.sety(self.y)
#         t.down()
#         t.circle(self.radius)
#         t.up()
#
#
# class Square(Shape):
#
#     def draw_shape(self):
#         t.setx(self.x)
#         t.sety(self.y)
#         t.down()
#         t.forward(self.radius * 2)
#         t.right(90)
#         t.forward(self.radius * 2)
#         t.right(90)
#         t.forward(self.radius * 2)
#         t.right(90)
#         t.forward(self.radius * 2)
#         t.right(90)
#         t.up()
#
#
# my_square = Square(0, 0, 25)
# my_circle = Circle(25, 25, 25)
# my_square.draw_shape()
# my_circle.draw_shape()
# t.done()


# Example_3

# def animals_say_hello(animal):
#     print(animal.say_hi())
#
#
# class Animal:
#     def say_hi(self):
#         pass
#
#
# class Cat(Animal):
#     def say_hi(self):
#         return 'Meow'
#
#
# class Dog(Animal):
#     def say_hi(self):
#         return 'Bow'
#
#
# cat = Cat()
# dog = Dog()
#
# animals_say_hello(cat)
# animals_say_hello(dog)


# Example_4

# class Test:
#     _x = 1
#     __x = 2
#
#
# x = Test()
#
# x._x
#
# print(x._x)
#
# x.__x
#
# print(x._Test__x)


# Example_5

# x = 1
# y = 2
# z = x + y
# print(x)
#
#
# class MyNum:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         if not isinstance(other, type(self)):
#             raise ValueError('wrong type for operand')
#         return MyNum(self.value + other.value)
#
#     def __str__(self):
#         return f'<MyNum: {self.value}>'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# x = MyNum(1)
# y = MyNum(2)
#
# print(x + y)
