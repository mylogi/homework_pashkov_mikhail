import random

#
# print(random.randint(1, 6))

print("Let`s play rock, paper, scissors")
player = input("Chose rock, paper, or scissors by typing r, p, or s: ")
if player == 'r' or player == 'p' or player == 's':
    computer = random.randint(1, 3)
    # 1 = r
    # 2 = p
    # 3 = s
    if computer == 1 and player == 'r' or computer == 2 and player == 'p' or computer == 3 and player == 's':
        print("It is a draw")
    elif computer == 1 and player == 'p' or computer == 2 and player == 's' or computer == 3 and player == 'r':
        print("Congratulations, you win!")
    else:
        print("You lost!")
    # elif (computer == 1 and player == 's' or computer == 2 and player == 'r' or computer == 3 and player == 'p'):
    #     print("Computer win!")
else:
    print("Your input was in the format, no game for you")
