"""

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


def stop_words(words: list):

    pass

 

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

 

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

"""


# Solution:

def stop_words(words: list):
    def inner_1(func):
        def wrapper(*args, **kwargs):
            result = func(*args)
            new_result = result
            for i in words:
                if i in result:
                    new_result = new_result.replace(i, '*')
            print(new_result)

        return wrapper

    return inner_1


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    create_slogan('Steve')
