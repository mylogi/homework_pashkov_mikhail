"""

Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of
Stack.

"""


# Solution:

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for item in self._items:
            representation += f'{item}'
        return representation

    def __str__(self):
        return self.__repr__()


def reverse(input_string) -> None:
    input_string = str(input_string)
    stack = Stack()
    for item in input_string:
        stack.push(item)
    while len(stack._items) > 0:
        char = stack.pop()
        print(char)
    print('\n')


def main():
    reverse('Hello')
    reverse('New world')
    reverse(1234567)


if __name__ == '__main__':
    main()
