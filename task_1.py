# We assume that all lists passed to functions are same length N

# Answers:

# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n

def question1(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


print(question1([1, 2, 3], [2, 4, 5]))


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


print(question2(2))


def question3(first_list: list[int], second_list: list[int]) -> list[int]:
    temp: list[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


print(question3([[6, 7], [6, 7, 5], 2, 3], [6, 7, 5]))


def question4(input_list: list[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


print(question4([0, 1, 2, 3, 4, 5]))


def question5(n: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


print(question5(2))


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


print(question6(6))
