import guess_art
import random
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

print(guess_art.logo)

hiddennumber = random.randint(0, 100)

choice = input("Choose game difficulty 'easy' 'hard': ").lower()

if choice == 'easy':
    life = 10
elif choice == 'hard':
    life = 5
else:
    print("Choose again.")

while life != 0:
    guess = int(input("Guess the Number: "))
    if guess != hiddennumber:
        life -= 1
        if guess > hiddennumber:
            print("Too High.")
        else:
            print("Too Low.")
    elif guess == hiddennumber:
        life = 0

if guess != hiddennumber:
    print(f"You Loose, the correct number is {hiddennumber}")
elif guess == hiddennumber:
    print(f"Your guess is right! The number is {hiddennumber}")
