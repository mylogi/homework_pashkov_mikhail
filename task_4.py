""" Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality
for saving messages to file

```

class CustomException(Exception):

def __init__(self, msg):

...

"""


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", 'a') as f:
            f.write(f'{self.msg}\n')


def main():
    raise CustomException('test for test')


if __name__ == '__main__':
    main()
