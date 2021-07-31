#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import necesary modules
from art import logo
import random

# Print Logo
print(logo)

# 1 Generate Ransome number
random_number = random.randint(1,100)

# Welcome text
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# 2 Create dictionary with number of options depending on name and assign to variable for number of attempts
difficulty_options = {'easy': 10, 'hard': 5}
attempts = difficulty_options[difficulty]

# Cheat to test
#print(random_number)

def review_attempts(attempts):
    if attempts > 0:
        return True
    else:
        return False

# 3 Create a function that determines the outcome of the guess
def evaluate_guess(attempts, random_number):
    found = False
    while attempts > 0 and found == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == random_number:
            found = True
        elif guess > 100:
            attempts -= 1
            if review_attempts(attempts):
                print("The guess needs to be between 1 and 100")
                print("Guess again")
        elif guess < random_number:
            attempts -= 1
            if review_attempts(attempts):
                print("Too low.")
                print("Guess again")
        elif guess > random_number:
            attempts -= 1
            if review_attempts(attempts):
                print("Too high")
                print("Guess again")
                
    return found


# 5 Execute function
if evaluate_guess(attempts, random_number):
    print("You win 😀")
else:
    print(f"You lose 😥, the number was: {random_number}")
