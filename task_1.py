"""The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

# Program_game:
import random


def game_data(random_number: int, user_number: int) -> bool:
    return random_number == user_number


def generate():
    print('Welcome in the Big Ten!')
    computer_number = random.randint(1, 10)
    user_input = int(input("Enter a number from 1 to 10: "))
    if user_input == 0 or user_input > 10:
        print('Incorrect input!')
    else:
        is_equal = game_data(computer_number, user_input)

        result = f'{user_input} - it`s right! You win!' if is_equal else 'You lost!'

        print(result)


if __name__ == '__main__':
    generate()
