"""Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:

    Addition
    Subtraction
    Division
    Multiplication
    Exponent (Power)
    Modulus
    Floor division
"""

# Program:

a = 4
b = 9

print('4 + 9 = ' + str(a + b))
print('4 - 9 = ' + str(a - b))
print('9 / 4 = ' + str(b / a))
print('9 ** 4 = ' + str(b ** a))
print('9 exponent 4 = ' + str(pow(b, a)))
print('9 % 4 = ' + str(b % a))
print('9 // 4 = ' + str(b // a))
