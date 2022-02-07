"""

Implement a queue using a singly linked list.

"""


# Solution:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

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
        return value

    def front_push(self, value):
        node = Node(value)
        cur = self.head.next
        # first_node = self.head
        while cur.next is not None:
            # first_node = cur
            cur = cur.next
        cur.next = node
        return value

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def get(self):
        cur = self.head.next
        first_node = self.head
        while cur.next is not None:
            first_node = cur
            cur = cur.next
        first_node.next = None
        return cur.value


def main():
    queue = Queue()
    print(f'Push: {queue.push(555)}')
    print(f'Push: {queue.push(444)}')
    print(f'Push: {queue.push(333)}')
    print(f'Push: {queue.push(222)}')
    print(f'Push: {queue.push(111)}')
    print(f"Queue: {queue}\n")
    print(f'Pop: {queue.pop()}')
    print(f'Peek: {queue.peek()}')
    print(f'Pop: {queue.pop()}')
    print(f"Queue: {queue}\n")

    # "Front push" is a method that adds an element to the front of the queue.
    print(f'Front push: {queue.front_push(11)}')
    print(f'Front push: {queue.front_push(12)}')
    print(f"Queue: {queue}\n")

    # "Get" is the method that removes the first element of the queue.
    print(f'Get: {queue.get()}')
    print(f'Push: {queue.push(66)}')
    print(f'Push: {queue.push(77)}')
    print(f"Queue: {queue}\n")

    # print(f'Pop: {queue.pop()}')
    # print(f'Pop: {queue.pop()}')
    # print(f'Pop: {queue.pop()}')
    # print(f'Get: {queue.get()}')
    # print(f'Get: {queue.get()}')
    # print(f'Get: {queue.get()}')
    # print(f"Queue: {queue}")


if __name__ == "__main__":
    main()
