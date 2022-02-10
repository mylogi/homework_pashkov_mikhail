"""

Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly
brackets are "balanced."

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
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f'{ind}: {item}\n'
        return representation

    def __str__(self):
        return self.__repr__()


def get_is_bracket_balanced(sentence_to_check: str) -> bool:
    stack = Stack()
    temp_dict = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for item in sentence_to_check:
        if item in temp_dict:
            stack.push(item)
        elif item in temp_dict.values():
            check_var = stack.pop()
            if item == temp_dict[check_var]:
                continue
            return False
    return True


if __name__ == '__main__':
    print(get_is_bracket_balanced('({[hello])}'))
    print(get_is_bracket_balanced('{([hello])}'))
    print(get_is_bracket_balanced('(){}[]'))

# @pytest.mark.parametrize(
#     ['input_value', 'expectation', ],
#     [
#         ('((hello))', True,),
#         ('({[hello]})', True,),
#         ('({[hello}])', False,),
#     ],
# )
# def test_balance_checker(input_value, expectation):
#     assert get_is_bracket_balanced(input_value) == expectation
