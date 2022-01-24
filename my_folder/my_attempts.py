# Example 1

# if False:
#     1 + "two"
# else:
#     1 + 2
#
# t = 1
# print(t, type(t))


# Example 2

# def function_for_ducks(duck):
#     dest = 'house'
#     print('Me:', 'Go to your house duck!')
#     print('Duck:', duck.walk(dest))
#     print('Me', 'Are you in house, duck?')
#     print('Duck:', duck.voice())
#     print('Me:', 'All good!')
#
#
# class Goose:
#     def walk(self, dest):
#         return f"duck walks to the {dest}"
#
#     def voice(self):
#         return "quack"
#
#
# d = Goose()
# print(type(d))
#
# function_for_ducks(d)


# Example 3

# from typing import Any, Optional, Tuple
#
#
# def test_type(x: Any, n: int = 10) -> Optional[Tuple[Any]]:
#     res: Tuple[Any] = tuple((x for _ in range(n)))
#     if res:
#         return res
#
#
# print(test_type('X'))
#
# print(test_type([1]))
#
# print(test_type(['test'], 0))


# Example 4

# class MyClass:
#     def __init__(self, a: int, b: str = ''):
#         self.a = a
#         self.b = b
#
#
# x = MyClass(1, 'hello')
# x_clone = MyClass(1, 'hello')
# y = MyClass(2, 'world')
#
# print(x)
# print(y)
#
# print(x == x_clone)
#
# q = MyClass(3)
# wrong = MyClass('2', 1)
# print(type(wrong.a))


# Example 5

# from dataclasses import dataclass
#
#
# @dataclass
# class MyClass:
#     a: int
#     b: str = ''
#
#
# x = MyClass(1, 'hello')
# x_clone = MyClass(1, 'hello')
# y = MyClass(2, 'world')
#
# print(x)
# print(y)
# print(x == x_clone)
#
# q = MyClass(3)
# wrong = MyClass('2', 1)
#
# print(q)
# print(wrong)


# Example 6

# from dataclasses import dataclass, asdict, astuple
#
#
# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
# class MyClass:
#     a: int = 1
#     b: int = 1
#
#
# @dataclass(init=True, repr=True, eq=True, order=True)
# class MyClass:
#     a: int = 1
#     b: int = 1
#
#
# x = MyClass(1, 1)
# y = MyClass(2, 1)
#
# print(x < y)
# print(astuple(x))
# print(astuple(y))
# print(astuple(x) < astuple(y))
# print(asdict(x))
#
#
# @dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
# class MyClass:
#     a: int = 1
#     b: int = 1
#
#
# x = MyClass(1, 1)
# x.a = 100
# x.c = 101


# Example 7

# from typing import List
# from dataclasses import dataclass, field
#
#
# @dataclass
# class C:
#     mylist: List[int] = field(default_factory=list)
#
# c = C()
# print('before', c.mylist)
# c.mylist += [1, 2, 3]
# print('after', c.mylist)


# Example 8

# from dataclasses import dataclass
# from typing import ClassVar
#
#
# @dataclass
# class MyClass:
#     a: int = 1
#     b: int = 1
#     cls_var: ClassVar = 0
#
#
# x = MyClass(2)
# print(x.__dict__)
# print(x.__class__.__dict__['cls_var'])
# print("Look at result:", x.a + x.b * x.cls_var)
#
#
# @dataclass
# class MyClass:
#     a: int = 1
#     b: int = 1
#     cls_var: ClassVar = 0
#
#     def very_cool_method(self):
#         return f"Look at result: {self.a + self.b * self.cls_var}"
#
#
# x = MyClass(2)
#
# print(x.very_cool_method())


# Example 9

# from dataclasses import dataclass
# from typing import ClassVar
#
#
# @dataclass
# class Base:
#     x: float = 15.0
#     y: int = 0
#
#
# @dataclass
# class C(Base):
#     z: int = 10
#     x: int = 15
#
#
# x = C()
# print(x)


# Example 10

# from dataclasses import dataclass, field
# from typing import ClassVar
#
#
# @dataclass
# class C:
#     a: float
#     b: float
#     c: float = field(init=False)
#
#     def __post_init__(self):
#         self.c = self.a + self.b
#
#
# x = C(2, 3)
# print(x.__dict__)
# print(x.c)


# Example 11

# from dataclasses import dataclass, field, InitVar
# from typing import ClassVar
#
#
# @dataclass
# class C:
#     a: float
#     b: float = None
#     c: InitVar[float] = 2.0
#
#     def __post_init__(self, c):
#         print('HERE', self.c, c)
#         self.b = self.a * c
#
#
# x = C(2, c=3.0)
# print(x.b)
# print(x.__dict__)


# Example 12

# from dataclasses import dataclass, field, InitVar, replace
# from typing import ClassVar
#
#
# @dataclass
# class C:
#     a: float
#     b: float = None
#     c: InitVar[float] = 2.0
#
#     def __post_init__(self, c):
#         print('HERE', self.c, c)
#         self.b = self.a * c
#
#
# x = C(2, c=3.0)
# # print(x.b)
# # print(x.__dict__)
#
# y = replace(x, a=4, c=3.0)
# print(y)
