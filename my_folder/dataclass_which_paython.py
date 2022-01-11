# def plain_class_example():
#     class T:
#         def __init__(self, n: int, f: float, s: str):
#             self.n = n
#             self.f = f
#             self.s = s
#
#     x = T(42, 4.5, 'hello')
#     x = T(42, f=4.5, s='hello')
#     y = x.n
#     x.n = 0
#
#
# def dataclass_example():
#     from dataclasses import dataclass
#
#     @dataclass
#     class T:
#         n: int
#         f: float
#         s: str
#
#     x = T(42, 4.5, 'hello')
#     x = T(24, f=4.5, s='hello')
#     y = x.n
#     x.n = 0


# class ManualComment:
#     def __init__(self, id: int, text: str):
#         self.__id: int = id
#         self.__text: str = text
#
#     @property
#     def id(self):
#         return self.__id
#
#     @property
#     def text(self):
#         return self.__text
#
#     def __repr__(self):
#         return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)
#
#     def __eq__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.id, self.text) == (other.id, other.text)
#         else:
#             return NotImplemented
#
#     def __neg__(self, other):
#         result = self.__eq__(other)
#         if result is NotImplemented:
#             return NotImplemented
#         else:
#             return not result
#
#     def __hash__(self):
#         return hash((self.__class__, self.id, self.text))
