"""Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

Tips: Use random module to get random char from string)
"""

# Program:
import random


def get_string(input_string: str) -> list[str]:
    result = []
    required_amount_of_words = len(input_string)
    while len(result) < required_amount_of_words:
        input_word_as_list = list(input_string)
        random.shuffle(input_word_as_list)
        new_word = ''.join(input_word_as_list)

        if new_word not in result:
            result.append(new_word)

    return result


def main():
    input_string = input('Enter your word: ')
    result = get_string(input_string=input_string)

    print('\n', result[0], result[1], result[2], result[3], result[4], sep='\n')


if __name__ == '__main__':
    main()
