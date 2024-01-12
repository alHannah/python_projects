import random
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    comphand = []
    condition1 = True
    condition2 = True

    compcard1 = random.choice(cards)
    compcard2 = random.choice(cards)

    for comp in range(1):
        comphand.append(compcard1)
        comphand.append(compcard2)
    
    print(f"COMPUTER: {compcard1}")



    playerhand = []
    playercard1 = random.choice(cards)
    playercard2 = random.choice(cards)

    for player in range(1):
        playerhand.append(playercard1)
        playerhand.append(playercard2)
    print(f"PLAYER: {playerhand}")

    while condition1:
        con = input("Do you want to add card?: ").lower()
        if con == "y":
            playerhand.append(random.choice(cards))
            print(f"PLAYER: {playerhand}")
        elif con == "n":
            condition1 = False
        


    print(f"COMPUTER: {comphand}")
    print(f"PLAYER: {playerhand}")

    playerscore = sum(playerhand)
    compscore = sum(comphand)

    while condition2:
        if compscore < 17:
            comphand.append(random.choice(cards))
        else:
            condition2 = False

    if playerscore > 21 or compscore > 21:
        playerscore = sum(playerhand) % 21
        compscore = sum(comphand) % 21
    else:
        print(compscore)
        print(playerscore)




    if playerscore > compscore:
        print("You WIN!")
    elif playerscore == compscore:
        print("DRAW")
    else:
        print("You LOOSE...")


condition = True
while condition:
    play = input("Do you eant to Play?: ").lower()
    if play == "n":
        condition = False
    elif play == "y":
        blackjack()
