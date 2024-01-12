import random
import word_list
import hangman_ascii
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

#This is the Hangman Game logo.
print(hangman_ascii.space)
print(hangman_ascii.logo)
print(hangman_ascii.space)
print(hangman_ascii.stages[6])

#Guess this random generated word
blank_word = random.choice(word_list.words)
#The integer length of the word
word_length = len(blank_word)

#List container
blank = []
#Displaying blanks
for _ in range(word_length):
    blank += "_"

#Combined blanks
the_blank = ' | '.join(blank)
#Showing the blanks
print(the_blank)

#Lives of the player
lives = 6
#Check if the game ended
game_end = False


#Loop of your guess letter until game end
while game_end == False:
    #Input form player of guess letter
    player_guess = input("\nGuess a letter: ").lower()
    clear()

    if player_guess in ''.join(blank):
        print("You already Guess this letter.")

    #The word left that is unknown
    for position in range(word_length):
        letter = blank_word[position]
        if letter == player_guess:
            blank[position] = letter

    #Guesses
    guessed = ' | '.join(blank)

    #Condition that you guess the incorrect letter
    if player_guess not in blank_word:
        lives -= 1
        #The ascii of your life left
        print(hangman_ascii.stages[lives])
        #The blanks
        print(guessed)
        #Condition that you Loose the Hangman Game
        if lives == 0:
            game_end = True
            print("\n\nYOU LOOSE THE GAME.")
            print(f"\nThe Blank is:\n{' | '.join(blank_word)}")
    else:
        #The ascii of your life left
        print(hangman_ascii.stages[lives])
        #The blanks
        print(guessed)
            
    #Condition that you win the Hangman Game.
    if ''.join(blank) == blank_word:
        game_end = True
        print("\n\nYOU WIN!")