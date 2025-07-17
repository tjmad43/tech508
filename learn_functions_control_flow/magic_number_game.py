# Practice control flow - Magic number guessing game
'''
# User story 1
As a user, I want to be able to guess a number and know if i
got it correct or not, so that I can know if I won or not.
# User story 2
As a user, I want to be able to guess a number and know if I need to go higher or lower.
# User story 3
As a user, I don't want my guesses wasted if I enter something accidentally
as my guess which are not digits.
# User story 4
As a user, after each guess, I would like to know how many guesses I have left.
# User story 5
As a user, I would like the magic to be randomly generated each time I play so it is more fun.
# User story 6
As a user, I would like to know the magic number at the end of the game if I still haven't guessed
correctly and I've used up all my tries.
'''
import random

# Define/assign number to a variable called magic_number
magic_number = random.randint(1, 100)

guesses = 5
game_end = False
while not game_end:
    # Allow the user 5 guesses
    while guesses > 0:
        # Ask user for input
        user_prompt = True
        while user_prompt:
            guess = input("Guess a number: ")
            if guess.isdigit():
                user_prompt = False
            else:
                print("Sorry, please type a number between 1 and 100. Try again.")
        # Check if this input matches magic_number
        # Let the user know if the response was correct or not
        if int(guess) == magic_number:
            print("Congratulations, you guessed the magic number!")
            print(f'You guessed in {5-guesses} guesses!')
            game_end = True
        elif int(guess) > magic_number:
            guesses -= 1
            print("Too high, try again.")
            print(f'You have {guesses} guesses left!')
        elif int(guess) < magic_number:
            guesses -= 1
            print("Too low, try again.")
            print(f'You have {guesses} guesses left!')
    print("Sorry, you ran out of guesses!")
    print(f'The magic number was {magic_number}')
    game_end = True


