"""Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


# Result:

def make_country():
    for k, v in d.items():
        print(k + ":", v)


d = {'Bosnia and Herzegovina': 'Sarajevo', 'Romania': 'Buharest', 'USA': 'Washington', 'Ukraine': 'Kyiv'}

if __name__ == '__main__':
    make_country()
