"""

Implement a stack using a singly linked list.

"""


# Solution:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):

        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


def main():
    stack = Stack()
    stack.push(323)
    stack.push(23)
    stack.push(111)
    stack.push(32)
    stack.push(3)
    print(f"Stack: {stack}")
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(f"Stack: {stack}")


if __name__ == "__main__":
    main()
