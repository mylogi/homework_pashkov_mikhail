# Create a python program named “task2”,
# and use the built-in function `print` in it several times.
# Try to pass “sep”, “end” params and pass several parameters separated by commas.
# Also, provide a comment text above each print statement,
# mentioned above, with the expected output after execution of the particular print statement.

# Use `print` in different ways

# Hello, world!; Hello world; Hello world; Hello, Bob!
print('Hello, world!')

print('Hello world')

what = "Hello"
who = "world"
print(f'{what} {who}')

print("""Hello, Bob!""")

# Try to pass "sep"

# For readability
print('\n')
# 1|2|3
print(1, 2, 3, sep='|')

print(1, 2, 3, sep='\n')

print('Hello!', 'Hi!', 'Glad to see you!', sep='\t')

# Try to pass "end"
# For readability
print('\n')

print(1, 2, 3, end='\n' + '-' * 10)

print('\n')

print(1, 2, 3, end='\t' + "-" + '\t'"Thease are numbers")

# The end
