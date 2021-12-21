""" Make a program that has your name and the current day of the week stored as separate variables and then prints
a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”

Note that <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods for constructing result string.
"""

# Program:
# Variables:
name = "michael"
day = "tuesday"


def good_day():
    return print(f'"Good day {name.title()}! {day.title()} is a perfect day to learn some python."')


if __name__ == '__main__':
    good_day()
