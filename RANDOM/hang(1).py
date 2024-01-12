#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)

chosen_letter = random.choice(chosen_list)

guess_letter = input("Guess a letter: ")
guess = guess_letter.lower()


to_int = len(chosen_word)
i = 0

while to_int > 0:
    if guess == chosen_list[i]:
        print("True")
    else:
        print("False")
    i += 1
    to_int -= 1

print(chosen_word)