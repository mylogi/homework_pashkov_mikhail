"""

Implement binary search using recursion.

"""


def binary_search(list_bs: list, low, high, val: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if list_bs[mid] == val:
            return mid
        elif list_bs[mid] > val:
            return binary_search(list_bs, low, mid - 1, val)
        else:
            return binary_search(list_bs, mid + 1, high, val)
    else:
        return False


def main():
    lys = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 3
    # x = 8
    # x = 9
    result = binary_search(lys, 0, len(lys) - 1, x)
    print(f'Search result: {result}')


if __name__ == '__main__':
    main()
