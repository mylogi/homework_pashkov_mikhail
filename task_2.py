"""

Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential,
binary searches.

"""


# Fibonacci algorithm:

def fibonacci_search(lys, val):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    while fib_m < len(lys):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2
    index = -1
    while fib_m > 1:
        i = min(index + fib_m_minus_2, (len(lys) - 1))
        if lys[i] < val:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            index = i
        elif lys[i] > val:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        else:
            return i
    if (
            fib_m_minus_1
            and index < (len(lys) - 1)
            and lys[index + 1] == val
    ):
        return index + 1
    return -1


print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 8))

'''

If you have a sorted array that you want to search through without using the division operator, you can use either
jump search or Fibonacci search.

If you want to search through an unsorted array or to find the first occurrence of a search variable, the best option is
linear (sequential) search

If you want to search through a sorted array, there are many options of which the simplest and fastest method is binary
search.

'''
