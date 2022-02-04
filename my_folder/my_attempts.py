# Example 1:

# def fib_iterative(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
#
#
# def fib_recursive(n):
#     if n == 0 or n == 1:
#         return n
#     return fib_recursive(n - 1) + fib_recursive(n - 2)
#
#
# print(fib_iterative(int(input("what fib do you want?: "))))
# print(fib_recursive(int(input("what fib do you want?: "))))


# Example 2:

# def factorial(n):
#     print(n)
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(int(input("Give me a number to factorialize: "))))
