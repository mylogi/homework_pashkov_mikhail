from datetime import datetime
from functools import wraps


class WowClass:
    def __init__(self, inlist):
        self.inlist = inlist
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.inlist):
            raise StopIteration
        result = self.inlist[self.i]
        self.i += 1
        return result

    def __call__(self, function):
        @wraps(function)
        def wrapper():
            print(function() + next(self.my_generator()))

        return wrapper

    def my_generator(self):
        if self.i >= len(self.inlist):
            self.i = 0
        result = self.inlist[self.i]
        self.i += 1
        yield result

    def __add__(self, other):
        for item in other.inlist:
            self.inlist.append(item)
        print(self.inlist)

    def __enter__(self, *args, **kwargs):
        self.start_time = datetime.now()

    def __exit__(self, *args, **kwargs):
        print(f'Time in job: {datetime.now() - self.start_time}')

    def __get__(self, instance, owner):
        return self.__val

    def __set__(self, instance, value):
        if self.inlist[0] <= value <= self.inlist[1]:
            self.__val = value
            return
        raise ValueError("Wrong grade!")


class School:
    max_grade = WowClass([1, 9])


def main():
    a = WowClass([1, 2, 3, 4, 5, 99])

    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))
    # print(next(a.my_generator()))

    with WowClass([1, 2, 3]) as b:
        # print(next(b.my_generator()))
        for i in range(1000):
            print(i)
        # print(next(b.my_generator()))

    @a
    def my_func():
        return 5

    for i in range(15):
        my_func()

    for i in a:
        print(i)

    for i in a:
        print(i)

    a += WowClass([6, 7])

    s1 = School
    s1 = 2
    s1 = 10
    print(s1)


if __name__ == '__main__':
    main()
