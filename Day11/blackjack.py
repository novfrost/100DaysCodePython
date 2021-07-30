############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import *
import random
from os import system, name

# Create a list of all the possible cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to shuffle and get a card
def get_card(cards):
    return cards[random.randint(0,len(cards)-1)]

# Function to get the first pair of cards for the user
def first_draw():
    player_cards = []
    for i in range(2):
        player_cards.append(get_card(cards))
    return player_cards

def computer_game(computer_cards):
    while sum(computer_cards) < 17:
        computer_cards.append(get_card(cards))
    return computer_cards

def game_result(player_cards, computer_cards):
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    return player_score, computer_score

def show_cards(player_cards, computer_cards):
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def when_as(player_cards):
    for index, num in enumerate(player_cards):
        if num == 11:
            player_cards[index] == 1
    return player_cards

def blackjack():
    # Ask user if the want to blackjack
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == 'y':
        # Initial set of cards and scores
        player_cards = []
        player_score = 0

        computer_cards= []
        computer_score = 0

        # Show logo.
        print(logo)

        # Shuffle first cards
        player_cards = first_draw()
        player_score = sum(player_cards)

        computer_cards = first_draw()
        computer_score = sum(computer_cards)

        # Computer game
        computer_game(computer_cards)

        show_cards(player_cards, computer_cards)

        more_cards = True

        while more_cards:
            if sum(player_cards) == 21:
                show_cards(player_cards, computer_cards)
                print("You win")
                blackjack()
            else:
                extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if extra_card == 'n':
                    scores = game_result(player_cards, computer_cards)
                    if scores[0] > scores[1] or scores[1] > 21:
                        print("You win")
                    else:
                        print("You lose")
                    more_cards = False
                    blackjack()
                else:
                    player_cards.append(get_card(cards))
                    player_score = sum(player_cards)

                    show_cards(player_cards, computer_cards)

                    if player_score > 21:
                        if 11 in player_cards:
                            when_as(player_cards)
                        else:
                            game_result(player_cards, computer_cards)
                            print("You lose!")
                            more_cards = False
                            blackjack()
                 
blackjack()
