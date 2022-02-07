""" Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two
parameters `start` and `stop`, and return a copy of the list starting at the position and going up to but not including
the stop position.

"""


# Solution:


class UnorderedList:

    def __init__(self):
        self.list_of_statements = []

    def add(self, item):
        self.list_of_statements.append(item)
        # self.list_of_statements.insert(0, item)

    def insert(self, index, item):
        self.list_of_statements.insert(index, item)
        return f"Index of insert's number: {self.list_of_statements.index(item)}"

    def index(self, item):
        return f"Index of {item=}: {self.list_of_statements.index(item)}"
        # index = 0
        # count = 0
        # for i in self.list_of_statements:
        #     if i == item:
        #         index += count
        #     else:
        #         count += 1
        # return index

    def pop(self, index=-1):
        return self.list_of_statements.pop(index)

    def slice(self, start_pos: int = 0, stop_pos: int = -1):
        return self.list_of_statements[start_pos:stop_pos]

    def __repr__(self):
        return str(self.list_of_statements)

    def __str__(self):
        return self.__repr__()


def main():
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list)
    print(my_list.index(31))
    print(my_list.insert(2, 42))
    print(my_list.pop())
    print(my_list)
    print(my_list.slice(0, 3))


if __name__ == "__main__":
    main()
