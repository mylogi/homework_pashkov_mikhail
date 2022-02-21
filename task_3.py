"""

Write a decorator `arg_rules` that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise,
return the result.

```

def arg_rules(type_: type, max_length: int, contains: list):

    pass



@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"



assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

```

"""


# Solution:

def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        def wrapper(name):
            # result = func(*args)
            if type(name) != type_:
                return False
            if len(name) > max_length:
                return False
            for z in contains:
                if name.find(z) > 0:
                    continue
                else:
                    return False
            return func(name)

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('johndoe05@gmail.com') is False)
    print(create_slogan('S@SH05') == "S@SH05 drinks pepsi in his brand new BMW!")
