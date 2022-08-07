from replit import clear
import random
import hangman_words
#- Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages

## print the header
print(logo)

#Update the word list to use the 'word_list' from hangman_words.py
# Choose a random word from the 'word_list'
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)]

## alternative way ##
# from hangman_words import word_list
# chosen_word = random.choice(word_list)


# define the game
end_of_game = False
lives = 6


# Create display presentation as [_ _ _ _]
display = []

for _ in range(word_length):
    display += "_"

# Looping for guessing the letter 
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed '{guess}' before.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong. (lose 1 life, and print out the letter and let them know it's not in the word.)
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The correct answer is '{chosen_word}'.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and this can lively show how many lives the hangman has.
    print(stages[lives])
    
