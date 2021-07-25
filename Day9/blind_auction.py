from art import *
from os import system

# Show Logo
print(logo)

# Create empty dicionary for bids
bids_dictionary = {}

# Create function to add bids
def add_to_bids_dictionary(name, bid):
    bids_dictionary[name] = bid

# Define a variable for the while loop to keep asking for bids
keep_biding = True

while keep_biding:

    # Ask the user for name and bid
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # Add data to the dictionary
    add_to_bids_dictionary(name, bid)

    # Ask if there are more bids
    user_response = input("Is there another bid? yes, no: \n")

    if user_response.lower() == 'no':
        keep_biding = False

    system('clear')


# Find the highest bid
winner_name = ''
highest_bid = 0
for key, value in bids_dictionary.items():
    if value > highest_bid:
        highest_bid = value
        winner_name = key

print(f"The winner of the auction is {winner_name} with a bid of ${highest_bid}")

