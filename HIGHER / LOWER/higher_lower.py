import random
import os
from art import logo, vs
from game_data import data


# short hand if else statement
# if os.name == 'posix':
#     'clear'
# else:
#     'cls'


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')



points = 0
game = True

randb = random.choice(data)


def format(choice):
    # calling from dictionary
    name = choice['name']
    description = choice['description']
    country = choice['country']
    # f string format for calling variables
    return (f"{name}, a {description}, from {country}.")

def score():
    if points != 0:
        print(f"You're right! Current score: {points}")

def check(guess, followera, followerb):
    if followera < followerb:
        return guess == "a"
    else:
        return guess == "b"

while game:
    print(logo)
    score()

    """Generate random from list"""
    randa = randb
    randb = random.choice(data)

    # to prevent same random comparison in the picker
    if randa == randb:
        randb = random.choice(data)

    print(f"Compare A: {format(randa)}")
    print(vs)
    print(f"Against B: {format(randb)}")

    followera = randa["follower_count"]
    followerb = randb["follower_count"]

    guess = input("Who has more followers?: ").lower()

    """Score feedback"""
    right_ans = check(guess, followera, followerb)
    if right_ans:
        points +=1
    else:
        game = False
        print(f"Sorry, that's wrong. Final score: {points}")

        