"""The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then
responds with a message accordingly.

"""

# Program:
import random


def first_expression(first_variable=random.randint(0, 1000), second_variable=random.randint(0, 1000)) -> dict:
    return {
        f'{first_variable} + {second_variable} =': first_variable + second_variable
    }


def second_expression(first_variable=random.randint(0, 100), second_variable=random.randint(0, 100)) -> dict:
    return {
        f'{first_variable} * {second_variable} =': first_variable * second_variable
    }


def third_expression(first_variable=random.randint(0, 1000), second_variable=random.randint(0, 1000)) -> dict:
    return {
        f'{first_variable} // {second_variable} =': first_variable // second_variable
    }


def give_first_expression():
    first_dictionary = first_expression()
    for key, value in first_dictionary.items():
        tool_1 = key
        tool_2 = value
        print(f'Hello, please solve this expression:\n{tool_1}')
        answer_first_expression = input('Enter your answer:')
        while answer_first_expression != tool_2:
            new_attempt = input('Slip! Try again.\nEnter your answer (maybe numbers): ')
            if new_attempt.isdigit() and int(new_attempt) == tool_2:
                print('Yeah! Its right!')
                break
        else:
            print('Yeah! Its right!')


def give_second_expression():
    second_dictionary = second_expression()
    for key_2, value_2 in second_dictionary.items():
        tool_1_second = key_2
        tool_2_second = value_2
        print(f'Please solve next expression:\n{tool_1_second}')
        answer_first_expression = input('Enter your answer:')
        while int(answer_first_expression) != tool_2_second:
            new_attempt_2 = input('Slip! Try again.\nEnter your answer (maybe numbers): ')
            if new_attempt_2.isdigit() and int(new_attempt_2) == tool_2_second:
                print('Yeah! Its right!')
                break
        else:
            print('Yeah! Its right!')


def give_third_expression():
    third_dictionary = third_expression()
    for key_3, value_3 in third_dictionary.items():
        tool_1_third = key_3
        tool_2_third = value_3
        print(f'Please solve next expression:\n{tool_1_third}')
        answer_first_expression = input('Enter your answer:')
        while int(answer_first_expression) != tool_2_third:
            new_attempt_3 = input('Slip! Try again.\nEnter your answer (maybe numbers): ')
            if new_attempt_3.isdigit() and answer_first_expression.isdigit() and int(new_attempt_3) == tool_2_third:
                print('Yeah! Its right!\nCongratulations - You win!')
                break
        else:
            print('Yeah! Its right!\nCongratulations - You win!')


def main():
    give_first_expression()
    give_second_expression()
    give_third_expression()


if __name__ == '__main__':
    main()
