# Import files and modules
import random
import os
from art import *
from game_data import data

# Define acumulator
number_correct_guess = 0

# Define criteria
correct_guess = True

# Validate when there is the same people being compared
def check_for_same_people(people_1, people_2):
    if people_1 == people_2:
        return True
    else:
        return False

# Create a function that compares
def compare_people(people_1=None, people_2=None):
    
    # Get Random data for the start of the game
    if people_1 == None:
        people_1 = random.randint(0, len(data)-1)
        people_2 = random.randint(0, len(data)-1)
        if check_for_same_people(people_1, people_2):
            people_2 = random.randint(0, len(data)-1)
    else:
        people_2 = random.randint(0, len(data)-1)
        if check_for_same_people(people_1, people_2):
            people_2 = random.randint(0, len(data)-1)
    
    return people_1, people_2


def show_comparison(people_1=None, number_correct_guess=0, correct_guess=True):

    while correct_guess:
        people = compare_people(people_1)
        if number_correct_guess != 0:
            print(logo)
            print(f"You're right! Current socre: {number_correct_guess}")
        else:
            print(logo)

        # Show first person
        print(f"Compare A: {data[people[0]]['name']}, a {data[people[0]]['description']} from {data[people[0]]['country']}")
        print(vs)
        print(f"Against B: {data[people[1]]['name']}, a {data[people[1]]['description']} from {data[people[1]]['country']}")

        # Get followe count
        follower_count_a = data[people[0]]['follower_count']
        follower_count_b = data[people[1]]['follower_count']

        highest_count_people = 0
        if follower_count_a > follower_count_b:
            highest_count = 0
        else:
            highest_count = 1

        user_guess = input("Who has more followers= Type 'A' or 'B': ")
        if user_guess.upper() == 'A':
            user_guess = 0
        else:
            user_guess = 1

        if user_guess == highest_count:
            os.system('cls' if os.name == 'nt' else 'clear')
            number_correct_guess += 1
            people_1 = people[highest_count]
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {number_correct_guess}")
            print(f"{data[people[0]]['name']}: {data[people[0]]['follower_count']}")
            print(f"{data[people[1]]['name']}: {data[people[1]]['follower_count']}")
            correct_guess = False

show_comparison()