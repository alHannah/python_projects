import blackj_art
import random
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def lplay():
    condition = True
    computerhand = []
    playerhand = []

    print(blackj_art.logo)

    for card in range(2):
        playercard = random.choice(cards)
        playerhand.append(playercard)
    playerscore = sum(playerhand)
    print(f"Player: {playerhand}    Score: {playerscore}")

    computercard = random.choice(cards)
    computerhand.append(computercard)
    computerscore = sum(computerhand)
    print(f"Computer: {computerhand}    Score: {computerscore}")

    if playerscore == 21:
        condition = False

    while condition:
        con = input("Do you want to add card?: ").lower()
        if con == "y":
            playercard = random.choice(cards)
            playerhand.append(playercard)
            playerscore = sum(playerhand)
            if 11 in playerhand and playerscore > 21:
                playerscore -= 10
            print(f"\nPlayer: {playerhand}    Score: {playerscore}")
            print(f"Computer: {computerhand}    Score: {computerscore}")
            if playerscore == 21:
                condition = False
            if playerscore > 21:
                condition = False
        elif con == "n":
            condition = False
            
    while computerscore < 17:
        computercard = random.choice(cards)
        computerhand.append(computercard)
        computerscore = sum(computerhand)
        print(f"\nPlayer: {playerhand}    Score: {playerscore}")
        print(f"Computer: {computerhand}    Score: {computerscore}")

    if playerscore == 21 and computerscore == 21:
        print("\nWIN")
    elif playerscore == 21:
        print("\nWIN")
    elif computerscore > 21 and computerscore > playerscore:
        print("\nWIN")
    elif playerscore == computerscore:
        print("\nTIE")
    elif playerscore > 21:
        print("\nLOOSE")
    elif playerscore > computerscore:
        print("\nWIN")
    else:
        print("\nLOOSE")


condition = True
while condition:
    play = input("Do you want to Play?: ").lower()
    if play == "n":
        condition = False
        clear()
    elif play == "y":
        clear()
        lplay()